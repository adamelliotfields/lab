import io

import matplotlib.pyplot as plt

from IPython.display import display_jpeg
from keras import ops


# displays images from a TensorFlow Dataset
def show_dataset_images(
    ds,
    rows=1,
    size=2,
    columns=5,
    figsize=None,
    unbatch=False,
    label_decoder=None,
):
    if figsize is None:
        figsize = (columns * size, rows * size)

    fig, axes = plt.subplots(rows, columns, figsize=figsize)

    if unbatch:
        ds = ds.unbatch()

    for i, (image, label) in enumerate(ds.take(rows * columns)):
        cmap = "gray" if image.shape[-1] == 1 else None
        ax = axes[i // columns, i % columns] if rows > 1 else axes[i]
        ax.imshow(ops.squeeze(image), cmap=cmap)
        if label_decoder is not None:
            ax.set_title(label_decoder(ops.squeeze(label)))
        else:
            ax.set_title(ops.argmax(label).numpy() if label.shape.ndims > 0 else label.numpy())
        ax.axis("off")

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
