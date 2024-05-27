import matplotlib.pyplot as plt
import seaborn as sns


# {
#   "history": {
#     "accuracy": [],
#     "loss": [],
#     "val_accuracy": [],
#     "val_loss": []
#   }
# }
def plot_keras_history(
    history,
    title="",
    metrics=None,
    x_ticks=None,
    markers=False,
):
    _, ax1 = plt.subplots()
    ax1.set_ylabel("Loss")
    ax1.set_xlabel("Epoch")

    if x_ticks is not None:
        ax1.set_xticks(x_ticks)

    sns.lineplot(
        history.history["loss"],
        ax=ax1,
        label="Train Loss",
        marker="o" if markers else None,
        color="blue",
        dashes=False,
        legend=False,
    )
    sns.lineplot(
        history.history["val_loss"],
        ax=ax1,
        label="Val Loss",
        marker="s" if markers else None,
        color="red",
        dashes=False,
        legend=False,
    )

    ax2 = ax1.twinx()
    ax2.set_ylabel("Accuracy")

    sns.lineplot(
        history.history["accuracy"],
        ax=ax2,
        label="Train Accuracy",
        marker="D" if markers else None,
        color="orange",
        dashes=False,
        legend=False,
    )
    sns.lineplot(
        history.history["val_accuracy"],
        ax=ax2,
        label="Val Accuracy",
        marker="^" if markers else None,
        color="green",
        dashes=False,
        legend=False,
    )

    # combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc="center right")

    # add text above legend
    if metrics is not None:
        plt.gcf().text(
            0.8875,
            0.625,
            f"Test Loss: {metrics[0]:.2}\nTest Accuracy: {metrics[1]:.2}",
            horizontalalignment="right",
            verticalalignment="center",
        )

    plt.title(title)
    plt.show()
