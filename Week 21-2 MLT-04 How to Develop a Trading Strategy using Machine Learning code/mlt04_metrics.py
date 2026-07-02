"""
Evaluation metrics and reporting for walk-forward cross-validation.

Functions:
- evaluate_walkforward_results: Generate performance summary DataFrame
- calculate_degradation: Compare train vs validation performance
- production_readiness_check: Validate model meets deployment criteria
"""

from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
)


def evaluate_walkforward_results(
    predictions: pd.Series, actuals: pd.Series, split_mccs: list[float] | None = None
) -> pd.DataFrame:
    """
    Generate comprehensive performance summary for walk-forward results.

    Parameters
    ----------
    predictions : pd.Series
        Model predictions (concatenated across all splits)
    actuals : pd.Series
        Actual labels (concatenated across all splits)
    split_mccs : Optional[List[float]], default=None
        MCC for each individual split (if available)

    Returns
    -------
    pd.DataFrame
        Performance metrics including:
        - MCC (Matthews Correlation Coefficient)
        - F1 Score
        - Precision
        - Recall
        - Accuracy
        - Confusion matrix components

    Examples
    --------
    >>> results = cv.run(model, X, y)
    >>> eval_df = evaluate_walkforward_results(
    ...     results['predictions'],
    ...     results['actuals'],
    ...     results['split_mccs']
    ... )
    >>> display(eval_df)

    Notes
    -----
    MCC is preferred over accuracy for imbalanced datasets:
    - Accuracy misleading when class distribution is 60/40 or worse
    - MCC ranges from -1 (perfect inverse) to +1 (perfect prediction)
    - MCC = 0 means random guessing (even with class imbalance)

    MCC Interpretation:
    - 1.0: Perfect prediction
    - 0.5: Strong predictive power (excellent for trading)
    - 0.3: Moderate edge (tradeable with risk management)
    - 0.1: Weak signal (benchmark territory)
    - 0.0: Random guessing
    - -1.0: Perfect inverse
    """
    # Calculate aggregate metrics
    mcc = matthews_corrcoef(actuals, predictions)
    f1 = f1_score(actuals, predictions, average="weighted")
    precision = precision_score(actuals, predictions, average="weighted")
    recall = recall_score(actuals, predictions, average="weighted")
    accuracy = accuracy_score(actuals, predictions)

    # Confusion matrix
    cm = confusion_matrix(actuals, predictions)

    # Build summary DataFrame
    metrics = {
        "Metric": [
            "MCC",
            "F1 Score",
            "Precision",
            "Recall",
            "Accuracy",
            "True Negatives",
            "False Positives",
            "False Negatives",
            "True Positives",
            "Total Samples",
        ],
        "Value": [
            f"{mcc:.4f}",
            f"{f1:.4f}",
            f"{precision:.4f}",
            f"{recall:.4f}",
            f"{accuracy:.4f}",
            int(cm[0, 0]),
            int(cm[0, 1]),
            int(cm[1, 0]),
            int(cm[1, 1]),
            len(predictions),
        ],
    }

    eval_df = pd.DataFrame(metrics)

    # Add split-wise MCC statistics if available
    if split_mccs is not None:
        split_stats = pd.DataFrame(
            {
                "Metric": ["MCC (mean)", "MCC (std)", "MCC (min)", "MCC (max)", "Number of Splits"],
                "Value": [
                    f"{np.mean(split_mccs):.4f}",
                    f"{np.std(split_mccs):.4f}",
                    f"{np.min(split_mccs):.4f}",
                    f"{np.max(split_mccs):.4f}",
                    len(split_mccs),
                ],
            }
        )
        eval_df = pd.concat([eval_df, split_stats], ignore_index=True)

    return eval_df


def calculate_degradation(
    train_mcc: float, validation_mcc: float, threshold: float = 0.20
) -> dict[str, Any]:
    """
    Calculate performance degradation from train to validation set.

    Parameters
    ----------
    train_mcc : float
        MCC on training set (walk-forward cross-validation)
    validation_mcc : float
        MCC on validation set (holdout)
    threshold : float, default=0.20
        Acceptable degradation threshold (e.g., 0.20 = 20%)

    Returns
    -------
    results : Dict[str, Any]
        Dictionary containing:
        - 'degradation_pct': float - Percentage degradation
        - 'degradation_abs': float - Absolute degradation
        - 'acceptable': bool - Whether degradation is within threshold
        - 'verdict': str - Human-readable verdict

    Examples
    --------
    >>> deg = calculate_degradation(
    ...     train_mcc=0.22,
    ...     validation_mcc=0.18,
    ...     threshold=0.20
    ... )
    >>> print(deg['verdict'])
    '✅ ACCEPTABLE: 18.2% degradation (within 20% threshold)'

    Notes
    -----
    Degradation Analysis:
    - < 10%: Excellent generalization (rare in finance)
    - 10-20%: Acceptable generalization (typical for good models)
    - 20-30%: Marginal (consider feature re-engineering)
    - > 30%: Overfit (return to feature engineering phase)

    Why Degradation Matters:
    - Training set seen 100+ times during development (high overfitting risk)
    - Validation set held out until final test (honest performance estimate)
    - Degradation > threshold indicates model memorized training noise
    """
    # Calculate degradation
    degradation_abs = train_mcc - validation_mcc
    degradation_pct = degradation_abs / train_mcc if train_mcc != 0 else float("inf")

    # Determine acceptability
    acceptable = degradation_pct <= threshold

    # Generate verdict
    if acceptable:
        verdict = (
            f"✅ ACCEPTABLE: {degradation_pct:.1%} degradation (within {threshold:.0%} threshold)"
        )
    else:
        verdict = (
            f"❌ OVERFIT: {degradation_pct:.1%} degradation (exceeds {threshold:.0%} threshold)"
        )

    return {
        "train_mcc": train_mcc,
        "validation_mcc": validation_mcc,
        "degradation_pct": degradation_pct,
        "degradation_abs": degradation_abs,
        "threshold": threshold,
        "acceptable": acceptable,
        "verdict": verdict,
    }


def production_readiness_check(
    validation_mcc: float,
    degradation_pct: float,
    sharpe_ratio: float | None = None,
    max_drawdown: float | None = None,
    verbose: bool = True,
) -> dict[str, Any]:
    """
    Validate model meets production deployment criteria.

    Parameters
    ----------
    validation_mcc : float
        MCC on validation set
    degradation_pct : float
        Degradation from train to validation (0-1 scale)
    sharpe_ratio : Optional[float], default=None
        Risk-adjusted return metric (if available)
    max_drawdown : Optional[float], default=None
        Maximum drawdown percentage (if available)
    verbose : bool, default=True
        Print detailed checklist

    Returns
    -------
    results : Dict[str, Any]
        Dictionary containing:
        - 'ready_for_production': bool - Overall readiness
        - 'checks_passed': int - Number of checks passed
        - 'checks_total': int - Total number of checks
        - 'checklist': Dict[str, bool] - Individual check results

    Examples
    --------
    >>> readiness = production_readiness_check(
    ...     validation_mcc=0.18,
    ...     degradation_pct=0.15,
    ...     sharpe_ratio=1.8,
    ...     max_drawdown=0.15
    ... )
    >>> print(f"Ready: {readiness['ready_for_production']}")
    Ready: True

    Notes
    -----
    Production Criteria (Conservative):
    - ✅ MCC > 0.15 (meaningful edge over random)
    - ✅ Degradation < 20% (acceptable generalization)
    - ✅ Sharpe > 1.5 (risk-adjusted profitability)
    - ✅ Max Drawdown < 20% (manageable risk)

    Additional Production Requirements (not checked here):
    - Transaction cost modeling (slippage, commissions)
    - Event-driven backtesting (realistic execution)
    - Live data integration (real-time feeds)
    - Position sizing (risk management)
    """
    checklist = {}

    # Check 1: MCC threshold
    checklist["mcc_above_0.15"] = validation_mcc > 0.15

    # Check 2: Degradation threshold
    checklist["degradation_below_20pct"] = degradation_pct < 0.20

    # Check 3: Sharpe ratio (if provided)
    if sharpe_ratio is not None:
        checklist["sharpe_above_1.5"] = sharpe_ratio > 1.5

    # Check 4: Max drawdown (if provided)
    if max_drawdown is not None:
        checklist["max_dd_below_20pct"] = max_drawdown < 0.20

    # Calculate overall readiness
    checks_passed = sum(checklist.values())
    checks_total = len(checklist)
    ready_for_production = all(checklist.values())

    if verbose:
        print("=" * 60)
        print("🚀 PRODUCTION READINESS CHECKLIST")
        print("=" * 60)

        print(f"\n✅ MCC > 0.15: {checklist['mcc_above_0.15']}")
        print(f"   Actual: {validation_mcc:.3f}")

        print(f"\n✅ Degradation < 20%: {checklist['degradation_below_20pct']}")
        print(f"   Actual: {degradation_pct:.1%}")

        if "sharpe_above_1.5" in checklist:
            print(f"\n✅ Sharpe > 1.5: {checklist['sharpe_above_1.5']}")
            print(f"   Actual: {sharpe_ratio:.2f}")

        if "max_dd_below_20pct" in checklist:
            print(f"\n✅ Max Drawdown < 20%: {checklist['max_dd_below_20pct']}")
            print(f"   Actual: {max_drawdown:.1%}")

        print("\n" + "=" * 60)
        print(f"RESULT: {checks_passed}/{checks_total} checks passed")

        if ready_for_production:
            print("✅ READY FOR PRODUCTION (subject to additional validation)")
        else:
            print("❌ NOT READY - Address failing checks before deployment")

        print("=" * 60)

        print("\n⚠️  ADDITIONAL REQUIREMENTS (not checked):")
        print("   - Transaction cost modeling (slippage, commissions)")
        print("   - Event-driven backtesting (Blueshift)")
        print("   - Live data integration (real-time feeds)")
        print("   - Position sizing and risk management")

    return {
        "ready_for_production": ready_for_production,
        "checks_passed": checks_passed,
        "checks_total": checks_total,
        "checklist": checklist,
        "validation_mcc": validation_mcc,
        "degradation_pct": degradation_pct,
    }
