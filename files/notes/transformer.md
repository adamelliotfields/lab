# Transformer (Attention is All You Need) [WIP]

![Transformer](../assets/transformer.png)
_Source: [Machine Learning Mastery](https://machinelearningmastery.com/the-transformer-model/)_

## Attention

At the heart of the Transformer is the concept of attention, a mechanism that allows models to focus on different parts (tokens) of the input sequence when performing a task, like predicting the next word in a sentence. This is akin to how humans can selectively focus on parts of a scene while ignoring others.

The evolution of attention mechanisms lead to the development of self-attention, which allows the model to weigh the importance of different parts of the input relative to each other. This is what allows the model to understand context. The introduction of multi-head attention allows the model to focus on different parts of the input sequence in parallel.

## Encoder-Decoder

The encoder-decoder architecture processes the input data through a series of encoder layers before passing it through the decoder layers to generate the output. In the figure above, the encoder is on the left (input) and the decoder is on the right (output).

Each encoder layer consists of a multi-head self-attention mechanism followed by a feed-forward neural network. The decoder layers also include a multi-head attention layer to focus on the relevant parts of the encoder's output.

This architecture enables Transformer models to process all of the input sequence simultaneously, making them highly parallelizable and efficient for training on large datasets. Coupled with the self-attention mechanism, models can capture long-range dependencies in the input sequence, which is crucial for tasks like machine translation.

## Resources

### Posts

* [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
* [DataCamp: How Transformers Work](https://www.datacamp.com/tutorial/how-transformers-work)
* [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
* [The GPT-3 Architecture, on a Napkin](https://dugas.ch/artificial_curiosity/GPT_architecture.html)

### Papers

* [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

### Videos

* [@3Blue1Brown](https://www.youtube.com/watch?v=wjZofJX0v4M)
* [@StatQuest](https://www.youtube.com/watch?v=zxQyTK8quyY)

### Notebooks

* [Neural Machine Translation with a Transformer and Keras](https://colab.research.google.com/github/tensorflow/text/blob/master/docs/tutorials/transformer.ipynb)
* [Sequence-to-Sequence Modeling with nn.Transformer and TorchText](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/transformer_tutorial.ipynb)
* [Illustrated: Self-Attention](https://colab.research.google.com/drive/1rPk3ohrmVclqhH7uQ7qys4oznDdAhpzF)
