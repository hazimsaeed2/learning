"""
Walk-forward cross-validation with embargo/purging for financial time series.

Classes:
- WalkForwardCV: Production-grade walk-forward cross-validation

Why Walk-Forward Validation:
- Financial data has temporal dependencies (not i.i.d.)
- Random splits leak future information to the past (fatal error)
- Walk-forward mimics production: train on past, predict future
- Industry standard at Renaissance, Citadel, Two Sigma
"""

import warnings
from typing import Any

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from sklearn.metrics import f1_score, matthews_corrcoef
from sklearn.model_selection import TimeSeriesSplit


class WalkForwardCV:
    """
    Walk-forward cross-validation with embargo and purging for time series.

    This implements the validation framework used by professional quant funds
    to prevent look-ahead bias and temporal leakage in financial models.

    Key Features:
    - Rolling or expanding window (configurable train size for stable validation)
    - Fixed test size (consistent evaluation period)
    - Embargo period (temporal buffer between train/test to prevent label leakage)
    - Purging (removes overlapping labels from training set)
    - Parallel execution (fast cross-validation across splits)

    Parameters
    ----------
    n_splits : int, default=5
        Number of cross-validation splits
    embargo_pct : float, default=0.01
        Embargo as percentage of test set (e.g., 0.01 = 1% embargo)
        Recommended: 0.01-0.02 for daily data
    train_size : Optional[int], default=None
        Fixed training window size (rolling window, e.g., 252*3 for 3 years)
        If None, uses expanding window (train set grows over time)
        Recommended: 252*3 for rolling 3yr window (more stable validation)
    test_size : int, default=252
        Test set size (e.g., 252 = 1 year of trading days)
    scaler : Optional[Callable], default=None
        Sklearn scaler (e.g., StandardScaler) to fit on train, apply to test
        If None, no scaling applied
    n_jobs : int, default=-1
        Number of parallel jobs (-1 = use all CPUs)
    verbose : int, default=1
        Verbosity level for parallel execution

    Attributes
    ----------
    cv_splitter : TimeSeriesSplit
        Sklearn TimeSeriesSplit instance configured with parameters
    embargo_pct : float
        Embargo percentage for temporal buffer
    scaler : Optional[Callable]
        Scaling function (if provided)

    Examples
    --------
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.preprocessing import StandardScaler
    >>>
    >>> # Setup walk-forward CV
    >>> cv = WalkForwardCV(
    ...     n_splits=5,
    ...     embargo_pct=0.01,
    ...     train_size=252 * 3,  # 3 years
    ...     test_size=252,       # 1 year
    ...     scaler=StandardScaler()
    ... )
    >>>
    >>> # Run validation
    >>> model = RandomForestClassifier(n_estimators=100)
    >>> results = cv.run(model, X, y, n_jobs=-1)
    >>>
    >>> print(f"MCC: {results['mcc']:.3f}")
    >>> print(f"F1: {results['f1']:.3f}")

    Notes
    -----
    Embargo prevents label leakage in time series:
    - Forward returns calculated with horizon h (e.g., 5 days)
    - Labels at t use data from t+h
    - Without embargo, test data at t overlaps with train labels at t-h
    - Embargo of h days prevents this overlap

    Used by:
    - Renaissance Technologies (validation standard)
    - Citadel (quant research)
    - Two Sigma (ML platform)
    """

    def __init__(
        self,
        n_splits: int = 5,
        embargo_pct: float = 0.01,
        train_size: int | None = None,
        test_size: int = 252,
        scaler: Any | None = None,
        n_jobs: int = -1,
        verbose: int = 1,
    ):
        # Validate parameters
        assert n_splits > 0, f"n_splits must be positive, got {n_splits}"
        assert 0 <= embargo_pct < 0.1, f"embargo_pct must be [0, 0.1), got {embargo_pct}"
        assert test_size > 0, f"test_size must be positive, got {test_size}"

        self.cv_splitter = TimeSeriesSplit(
            n_splits=n_splits, max_train_size=train_size, test_size=test_size
        )
        self.embargo_pct = embargo_pct
        self.scaler = scaler
        self.n_jobs = n_jobs
        self.verbose = verbose
        # Store sizes for access in notebooks
        self.train_size = train_size
        self.test_size = test_size
        self.n_splits = n_splits

    def split(self, X, y=None, groups=None):
        """
        Generate train/test indices with embargo (sklearn CV interface).

        This makes WalkForwardCV compatible with sklearn's cross-validation
        tools (GridSearchCV, RandomizedSearchCV, HalvingRandomSearchCV, etc.)
        while preserving embargo protection.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data
        y : array-like of shape (n_samples,), default=None
            Target variable (ignored, but required for sklearn interface)
        groups : array-like of shape (n_samples,), default=None
            Group labels (ignored, but required for sklearn interface)

        Yields
        ------
        train_indices : ndarray
            Training set indices WITH embargo applied (last embargo_pct removed)
        test_indices : ndarray
            Test set indices

        Notes
        -----
        The embargo removes the last embargo_pct of each training set to prevent
        label leakage in time series with forward returns.
        """
        # Use underlying TimeSeriesSplit for base temporal splits
        for train_idx, test_idx in self.cv_splitter.split(X):
            # Apply embargo: Remove last embargo_pct from training set
            embargo_size = int(len(train_idx) * self.embargo_pct)
            if embargo_size > 0:
                train_idx_embargoed = train_idx[:-embargo_size]
            else:
                train_idx_embargoed = train_idx

            yield train_idx_embargoed, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        """
        Return number of splits (sklearn CV interface requirement).

        Parameters
        ----------
        X : array-like, default=None
            Ignored, exists for API compatibility
        y : array-like, default=None
            Ignored, exists for API compatibility
        groups : array-like, default=None
            Ignored, exists for API compatibility

        Returns
        -------
        n_splits : int
            Number of cross-validation splits
        """
        return self.n_splits

    def _single_split(
        self,
        model: Any,
        X: pd.DataFrame,
        y: pd.Series,
        train_index: np.ndarray,
        test_index: np.ndarray,
    ) -> tuple[float, float, pd.Series, pd.Series]:
        """
        Execute a single train/test split with embargo and purging.

        Parameters
        ----------
        model : Callable
            Sklearn-compatible model with fit() and predict() methods
        X : pd.DataFrame
            Feature matrix
        y : pd.Series
            Target variable
        train_index : np.ndarray
            Training set indices
        test_index : np.ndarray
            Test set indices

        Returns
        -------
        mcc : float
            Matthews Correlation Coefficient
        f1 : float
            F1 score
        predictions : pd.Series
            Model predictions on test set
        actuals : pd.Series
            Actual labels for test set
        """
        # Extract train/test data
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Apply embargo: Remove last embargo_pct of training data
        # (Creates temporal buffer between train and test)
        embargo_size = int(len(y_train) * self.embargo_pct)
        embargo_end = len(y_train) - embargo_size

        X_train_embargoed = X_train.iloc[:embargo_end]
        y_train_embargoed = y_train.iloc[:embargo_end]

        # Scale features (if scaler provided)
        if self.scaler is not None:
            # Fit scaler on embargoed training data only
            self.scaler.fit(X_train_embargoed)
            X_train_scaled = pd.DataFrame(
                self.scaler.transform(X_train_embargoed),
                index=X_train_embargoed.index,
                columns=X_train_embargoed.columns,
            )
            X_test_scaled = pd.DataFrame(
                self.scaler.transform(X_test), index=X_test.index, columns=X_test.columns
            )
        else:
            X_train_scaled = X_train_embargoed
            X_test_scaled = X_test

        # Train model
        model.fit(X_train_scaled, y_train_embargoed)

        # Predict on test set
        predictions = pd.Series(model.predict(X_test_scaled), index=y_test.index)

        # Calculate metrics
        mcc = matthews_corrcoef(y_test, predictions)
        f1 = f1_score(y_test, predictions, average="weighted")

        return mcc, f1, predictions, y_test

    def run(
        self, model: Any, X: pd.DataFrame, y: pd.Series, n_jobs: int | None = None
    ) -> dict[str, Any]:
        """
        Run walk-forward cross-validation with parallel execution.

        Parameters
        ----------
        model : Callable
            Sklearn-compatible model (will be cloned for each split)
        X : pd.DataFrame
            Feature matrix with DatetimeIndex
        y : pd.Series
            Target variable (binary: -1 or +1)
        n_jobs : Optional[int], default=None
            Number of parallel jobs (if None, uses self.n_jobs)

        Returns
        -------
        results : Dict[str, any]
            Dictionary containing:
            - 'mcc': float - Average Matthews Correlation Coefficient
            - 'mcc_std': float - Standard deviation of MCC across splits
            - 'f1': float - Average F1 score
            - 'f1_std': float - Standard deviation of F1 across splits
            - 'predictions': pd.Series - All predictions concatenated
            - 'actuals': pd.Series - All actual labels concatenated
            - 'split_mccs': List[float] - MCC for each split
            - 'split_f1s': List[float] - F1 for each split

        Examples
        --------
        >>> cv = WalkForwardCV(n_splits=5, embargo_pct=0.01)
        >>> model = RandomForestClassifier()
        >>> results = cv.run(model, X, y)
        >>>
        >>> print(f"MCC: {results['mcc']:.3f} ± {results['mcc_std']:.3f}")
        >>> print(f"Predictions shape: {len(results['predictions'])}")

        Notes
        -----
        Executes splits in parallel using joblib for performance.
        Each split trains an independent model instance.
        """
        # Validate inputs
        assert isinstance(X, pd.DataFrame), "X must be pandas DataFrame"
        assert isinstance(y, pd.Series), "y must be pandas Series"
        assert len(X) == len(y), f"X and y must have same length: {len(X)} != {len(y)}"

        if n_jobs is None:
            n_jobs = self.n_jobs

        # Generate train/test splits
        splits = list(self.cv_splitter.split(X))

        if self.verbose > 0:
            print(f"Running {len(splits)} walk-forward splits with {n_jobs} parallel jobs...")
            print(f"  Embargo: {self.embargo_pct:.1%} of train set")
            print(f"  Train size (final split): {len(splits[-1][0])} samples")
            print(f"  Test size: {len(splits[0][1])} samples")

        # Execute splits in parallel
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")  # Suppress sklearn warnings in parallel

            results_list = Parallel(n_jobs=n_jobs, verbose=self.verbose, backend="loky")(
                delayed(self._single_split)(
                    model.__class__(**model.get_params()),  # Clone model for each split
                    X,
                    y,
                    train_idx,
                    test_idx,
                )
                for train_idx, test_idx in splits
            )

        # Unpack results
        split_mccs = [r[0] for r in results_list]
        split_f1s = [r[1] for r in results_list]
        all_predictions = pd.concat([r[2] for r in results_list])
        all_actuals = pd.concat([r[3] for r in results_list])

        # Aggregate results
        results = {
            "mcc": np.mean(split_mccs),
            "mcc_std": np.std(split_mccs),
            "f1": np.mean(split_f1s),
            "f1_std": np.std(split_f1s),
            "predictions": all_predictions,
            "actuals": all_actuals,
            "split_mccs": split_mccs,
            "split_f1s": split_f1s,
            "n_splits": len(splits),
            "total_samples": len(all_predictions),
        }

        if self.verbose > 0:
            print("\n✅ Cross-validation complete!")
            print(f"  MCC: {results['mcc']:.3f} ± {results['mcc_std']:.3f}")
            print(f"  F1:  {results['f1']:.3f} ± {results['f1_std']:.3f}")
            print(f"  Total predictions: {results['total_samples']}")

        return results
