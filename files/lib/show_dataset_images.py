import io

import matplotlib.pyplot as plt
import tensorflow as tf

from IPython.display import display_jpeg


# displays images from a TensorFlow Dataset
def show_dataset_images(
    ds,
    *,
    rows=1,
    size=2,
    columns=5,
    figsize=None,
    label_decoder=None,
):
    if figsize is None:
        figsize = (columns * size, rows * size)

    fig, axes = plt.subplots(rows, columns, figsize=figsize)

    for i, (image, label) in enumerate(ds.take(rows * columns)):
        image = image.numpy().squeeze()

        # rescale from -1, 1 to 0, 1
        if image.min() < 0:
            image = (image + 1) / 2

        # rescale to 0, 255 integers
        if not image.max() > 1:
            image = image * 255

        image = image.astype("uint8")
        ax = axes[i // columns, i % columns] if rows > 1 else axes[i]
        ax.imshow(image, cmap="gray" if image.shape[-1] == 1 else None)
        ax.axis("off")

        # if one-hot encoded
        label = tf.squeeze(label)
        if tf.rank(label) > 0:
            label = tf.argmax(label)

        if label_decoder is not None:
            ax.set_title(label_decoder(label))
        else:
            ax.set_title(f"{label}")

    # jpeg compress the figure to significantly reduce notebook size
    fig_buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(fig_buf, format="jpeg")
    plt.close(fig)

    # we now have a jpeg in memory, not a matplotlib figure
    # the pointer is at the end of the "file" in memory
    # need to move it back to the beginning for reading
    fig_buf.seek(0)
    display_jpeg(fig_buf.getvalue(), raw=True)
