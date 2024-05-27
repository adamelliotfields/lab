import numpy as np
import pandas as pd

from sklearn.utils import Bunch


def dataset_to_dataframe(dataset: Bunch, categorical=False):
    """Converts a Sklearn dataset to a Pandas DataFrame.\n
    Args:
        dataset (Bunch): Dataset with `data`, `target`, `feature_names`, and `target_names` attributes.
        categorical (bool, optional): Converts `target` column to categorical using `target_names`. Defaults to False.\n
    Returns:
        DataFrame: A Pandas DataFrame.
    """
    if dataset.target.ndim > 1:
        # linnerud (multi-output regression)
        target_columns = [f"target_{i}" for i in range(dataset.target.shape[1])]
    else:
        target_columns = ["target"]

    df = pd.DataFrame(
        np.c_[dataset.data, dataset.target],
        columns=np.append(dataset.feature_names, target_columns),
    )

    if categorical and dataset.target.ndim == 1 and hasattr(dataset, "target_names"):
        df[target_columns[0]] = pd.Categorical.from_codes(
            dataset.target,
            categories=dataset.target_names,
        )

    return df
