# Gradio Notes

Notes on building Gradio apps.

## API

Gradio turns your event handlers into API endpoints by default. For example:

```py
def on_predict_click(sepal_length, sepal_width, petal_length, petal_width):
    inputs = [[sepal_length, sepal_width, petal_length, petal_width]]
    probas = model.predict_proba(inputs)
    # return a tuple if you have multiple outputs
    return {name: proba for (name, proba) in zip(target_names, np.squeeze(probas))}

# inputs are the arguments to `fn`
# output components receive the return value of `fn`
predict_button.click(
    fn=on_predict_click,
    inputs=[sepal_length_slider, sepal_width_slider, petal_length_slider, petal_width_slider],
    outputs=[predict_label],
    api_name="predict",
)
```

Will result in a `/predict` endpoint. If we didn't set the name, it would default to the name of the function (`/on_predict_click`).

For any handlers you don't want to expose, you can set `show_api=False`. If you want to disable the API entirely, set `show_api=False` in `demo.launch()`.

### Loading 🤗 repositories

The API enables you to run Spaces from Hugging Face locally. The UI is run on your machine, but the processing is done remotely with the results sent over the API. It works for simple spaces as long as they are using the same major version of Gradio as you. You can also run model repos with a default UI based on the model's task.

```py
import gradio as gr

gr.load("HuggingFaceH4/zephyr-7b-beta", src="models").launch()
```

## Argument Parsing

Make your apps configurable with command line arguments:

```py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--lowvram",
    action='store_true',  # boolean flag, defaults to False
    help="Optimize settings for low VRAM",
)
args = parser.parse_args()

if args.lowvram:
    print("Low VRAM mode enabled")
```

For example:

```sh
python app.py --lowvram
```

## Environment Variables

To force sharing all the time, you can set the environment variable `GRADIO_SHARE=true`. Note that anything besides "True" or "true" does nothing.

If you are always setting a custom server and/or port, you can set `GRADIO_SERVER_NAME` and `GRADIO_SERVER_PORT`.

Use `GRADIO_DEFAULT_CONCURRENCY_LIMIT` to set the number of concurrent jobs from the queue.

## Reloading

To enable watch mode, run your app with `gradio app.py` instead of `python app.py`.

In watch mode, `launch` isn't called. A caveat to to this is that Gradio will expect your app to be named `demo`. If you cannot rename your app, then you must pass the name as a positional parameter like `gradio app.py my_app`.

Any code in a `if gr.NO_RELOAD` block will not be re-evaluated when the source file is reloaded.

## Queue

Gradio has a built-in queue that can scale to thousands of concurrent users. Enabling the queue is simply calling `demo.queue()` before `demo.launch()`.

The `default_concurrency_limit` keyword argument defaults to `1` and you can set it to an int or `None`. You can also set the maximum number of events stored in the queue with `max_size`. Finally, you can set `api_open=True` to allow API requests to skip the queue.

Each event handler has a `concurrency_limit` keyword argument that gives you more granular control over the number of concurrent jobs for each specific function.

The queue is required for Info and Warning alerts ("modals") and the Progress tracker.

## Errors

Simply `raise gr.Error("message")` anywhere to display an Error alert to the user. This does not require the queue to be enabled.

To show **all** application errors to users, use `show_error=True` in `demo.launch()`.

## Notebooks

You can run Gradio apps inside Jupyter (including VS Code) and Colab.

```py
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Hello!")
    inp = gr.Textbox()
    out = gr.Textbox()
    inp.change(fn=lambda x: x, inputs=inp, outputs=out)

demo.launch(quiet=True, debug=True, share=False)
```

The above runs the Gradio server until you stop the cell (debug mode), which is the equivalent of <kbd>Ctrl</kbd>+<kbd>C</kbd> in the terminal. Explicitly setting `share` silences the sharing suggestion (not silenced by `quiet`).

There is also a custom Jupyter magic:

```py
%load_ext gradio
```

```py
%%blocks
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Hello!")
    inp = gr.Textbox()
    out = gr.Textbox()
    inp.change(fn=lambda x: x, inputs=inp, outputs=out)
```

When run this way, the process runs in the background so you can make changes and <kbd>Shift</kbd>+<kbd>Enter</kbd> to update the UI quickly. To stop the server, you must explicitly call `demo.close()` in another cell.

### Colab

When run in Colab, share mode (`share=True`) will automatically be enabled. This creates a temporary public link and SSH tunnel. Note that every time you restart the server, it will generate a new public link.

## User History

Use [`wauplin/gradio-user-history`](https://huggingface.co/spaces/Wauplin/gradio-user-history) to give each user the ability to log in with their Hugging Face account and save their past image generations.

## Persistent Storage

Whatever you save to disk in a Space is ephemeral and will be lost when the Space restarts. You can subscribe to persistent disk storage for $5/mo or use the [Hub](https://github.com/huggingface/huggingface_hub) client to upload files to a Dataset that you want to preserve. You could use [APScheduler](https://github.com/agronholm/apscheduler) to run scheduled backups in this way.
