"""Reproducible time-aware EEG eye-state experiment.

The dataset is one chronological recording. We deliberately use contiguous
train/validation/test blocks rather than random row splitting.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.io import arff
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "EEG Eye State.arff"
RESULTS = ROOT / "results"
CHANNELS = ["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]


def load_data() -> tuple[np.ndarray, np.ndarray]:
    rows, _ = arff.loadarff(DATA)
    names = rows.dtype.names
    x = np.column_stack([rows[name].astype(float) for name in CHANNELS])
    target_name = [name for name in names if name not in CHANNELS][0]
    y = np.array([int(value.decode() if isinstance(value, bytes) else value) for value in rows[target_name]])
    return x, y


def trailing_features(x: np.ndarray, window: int = 9) -> np.ndarray:
    """Add causal trailing mean and standard deviation for each channel."""
    means = np.empty_like(x)
    stds = np.empty_like(x)
    for index in range(len(x)):
        start = max(0, index - window + 1)
        segment = x[start : index + 1]
        means[index] = segment.mean(axis=0)
        stds[index] = segment.std(axis=0)
    return np.hstack([x, means, stds])


def evaluate(name: str, x: np.ndarray, y: np.ndarray, train_end: int, val_end: int) -> dict:
    train = slice(0, train_end)
    validation = slice(train_end, val_end)
    test = slice(val_end, len(y))
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, class_weight="balanced"))
    model.fit(x[train], y[train])
    validation_probability = model.predict_proba(x[validation])[:, 1]
    test_probability = model.predict_proba(x[test])[:, 1]
    test_prediction = (test_probability >= 0.5).astype(int)
    return {
        "model": name,
        "train_samples": int(train_end),
        "validation_samples": int(val_end - train_end),
        "test_samples": int(len(y) - val_end),
        "validation_roc_auc": float(roc_auc_score(y[validation], validation_probability)),
        "test_roc_auc": float(roc_auc_score(y[test], test_probability)),
        "test_balanced_accuracy": float(balanced_accuracy_score(y[test], test_prediction)),
        "test_f1": float(f1_score(y[test], test_prediction)),
    }


def blocked_cross_validate(name: str, x: np.ndarray, y: np.ndarray, splits: int = 5) -> dict:
    """Evaluate contiguous future blocks using only earlier samples for fitting."""
    splitter = TimeSeriesSplit(n_splits=splits)
    folds = []
    for fold, (train_index, test_index) in enumerate(splitter.split(x), 1):
        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, class_weight="balanced"))
        model.fit(x[train_index], y[train_index])
        probability = model.predict_proba(x[test_index])[:, 1]
        prediction = (probability >= 0.5).astype(int)
        fold_result = {
            "fold": fold,
            "train_start": int(train_index[0]),
            "train_end_exclusive": int(train_index[-1] + 1),
            "test_start": int(test_index[0]),
            "test_end_exclusive": int(test_index[-1] + 1),
            "train_samples": int(len(train_index)),
            "test_samples": int(len(test_index)),
            "test_roc_auc": float(roc_auc_score(y[test_index], probability)),
            "test_balanced_accuracy": float(balanced_accuracy_score(y[test_index], prediction)),
            "test_f1": float(f1_score(y[test_index], prediction)),
        }
        folds.append(fold_result)
    aucs = np.array([fold["test_roc_auc"] for fold in folds])
    return {
        "model": name,
        "splitter": "sklearn TimeSeriesSplit",
        "fold_count": len(folds),
        "folds": folds,
        "summary": {
            "mean_test_roc_auc": float(aucs.mean()),
            "std_test_roc_auc": float(aucs.std(ddof=1)),
            "min_test_roc_auc": float(aucs.min()),
            "max_test_roc_auc": float(aucs.max()),
        },
    }


def main() -> None:
    x, y = load_data()
    train_end = int(len(y) * 0.70)
    val_end = int(len(y) * 0.85)
    results = {
        "dataset": {
            "name": "UCI EEG Eye State",
            "samples": int(len(y)),
            "channels": CHANNELS,
            "eye_closed_fraction": float(y.mean()),
            "split": "chronological 70% train / 15% validation / 15% test",
        },
        "models": [
            evaluate("pointwise EEG", x, y, train_end, val_end),
            evaluate("EEG + causal temporal context", trailing_features(x), y, train_end, val_end),
        ],
        "blocked_cross_validation": [
            blocked_cross_validate("pointwise EEG", x, y),
            blocked_cross_validate("EEG + causal temporal context", trailing_features(x), y),
        ],
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
