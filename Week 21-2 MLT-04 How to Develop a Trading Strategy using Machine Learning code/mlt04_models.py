"""Standard model configurations for consistent evaluation across notebooks.

CRITICAL: All notebooks MUST use these factories to ensure reproducible results.
Ad-hoc model configurations create inconsistent evaluations and confusing results.
"""

import lightgbm as lgb
from sklearn.dummy import DummyClassifier


def build_dummy_model(random_state: int = 42) -> DummyClassifier:
    """Build Tier 1 baseline (DummyClassifier).

    Args:
        random_state: Random seed for reproducibility

    Returns:
        Configured DummyClassifier instance
    """
    return DummyClassifier(strategy="prior", random_state=random_state)


def build_simple_model(random_state: int = 42) -> lgb.LGBMClassifier:
    """Build Tier 2 simple model (3 features: returns_1d, returns_5d, volatility_20d).

    Args:
        random_state: Random seed for reproducibility

    Returns:
        Configured LGBMClassifier instance
    """
    return lgb.LGBMClassifier(
        num_iterations=50, max_depth=5, verbose=-1, random_state=random_state, n_jobs=-1
    )


def build_microstructure_model(random_state: int = 42) -> lgb.LGBMClassifier:
    """Build Tier 3 microstructure model (11 features: basic + microstructure).

    Args:
        random_state: Random seed for reproducibility

    Returns:
        Configured LGBMClassifier instance
    """
    return lgb.LGBMClassifier(
        num_iterations=50,
        max_depth=10,
        min_child_samples=20,  # Use sklearn-style parameter (avoids conflict)
        verbose=-1,
        random_state=random_state,
        n_jobs=-1,
    )


def build_full_model(random_state: int = 42) -> lgb.LGBMClassifier:
    """Build full feature model (~108 features: 3 basic + 8 microstructure + ~97 TA-Lib derived).

    STANDARD CONFIGURATION for all full-feature evaluations.
    DO NOT create ad-hoc configurations - use this factory.

    Args:
        random_state: Random seed for reproducibility

    Returns:
        Configured LGBMClassifier instance
    """
    return lgb.LGBMClassifier(
        num_iterations=50,
        max_depth=10,
        min_child_samples=20,  # Use sklearn-style parameter (avoids conflict)
        verbose=-1,
        random_state=random_state,
        n_jobs=-1,
    )


def build_tuned_model(
    num_iterations: int, max_depth: int, min_child_samples: int, random_state: int = 42
) -> lgb.LGBMClassifier:
    """Build model with custom hyperparameters (for Module 4 tuning).

    Args:
        num_iterations: Number of boosting iterations
        max_depth: Maximum tree depth
        min_child_samples: Minimum samples per leaf (sklearn-style parameter)
        random_state: Random seed for reproducibility

    Returns:
        Configured LGBMClassifier instance
    """
    return lgb.LGBMClassifier(
        num_iterations=num_iterations,
        max_depth=max_depth,
        min_child_samples=min_child_samples,  # Use sklearn-style parameter (no conflict)
        verbose=-1,
        random_state=random_state,
        n_jobs=-1,
    )
