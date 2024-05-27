import pandas as pd

from scipy.stats import kurtosis, median_abs_deviation, skew


# adds additional Scipy stats to Pandas describe and returns a DataFrame
def describe_dataframe(df: pd.DataFrame, as_markdown=False):
    total = df.shape[0]  # len(df)

    additional_stats = pd.DataFrame(
        {
            "mode": df.apply(lambda x: x.mode()[0], axis=0),
            "range": df.apply(lambda x: x.max() - x.min(), axis=0),
            "IQR": df.apply(lambda x: x.quantile(0.75) - x.quantile(0.25), axis=0),
            "MAD": df.apply(lambda x: median_abs_deviation(x.dropna()), axis=0),
            "CV": df.apply(lambda x: x.std() / x.mean(), axis=0),
            "skewness": df.apply(lambda x: skew(x.dropna()), axis=0),
            "kurtosis": df.apply(lambda x: kurtosis(x.dropna(), fisher=True), axis=0),
            "unique": df.nunique(),
            "missing": df.isnull().sum(),
        }
    )

    # need to transpose (`T`)
    describe = df.describe(percentiles=[]).T.astype({"count": int})

    # rename
    describe.rename(columns={"count": f"count ({total})", "50%": "median"}, inplace=True)

    # merge
    describe = describe.join(additional_stats)

    # add dtypes after merging
    describe["dtype"] = df.dtypes

    # usage: IPython.display.Markdown(describe_dataframe(df, as_markdown=True))
    # requires `pip install tabulate` in your environment
    if as_markdown:
        return describe.to_markdown(floatfmt=".2f")

    return describe
