# ye-bot
Neural networks that take in character level rap lyrics and put out BARS. 

TODO: Implement [Combining Learned Lyrical Structures and Vocabulary for Improved Lyric Generation](https://arxiv.org/pdf/1811.04651.pdf#cite.vaswani17attention)

## Data Structure

structure folder
  - currently used

vocabulary folder
  - not currently used

## MODEL 1

### 
First refer to the data/README, and download or supply any data you wish to use.

Then spin up a Keras docker container, which automatically mounts this repository

```bash
make keras
```

From within the container, you can train the model with:

```bash
python3 character_level_lstm/recurrent_keras.py
```

You can visualize training with tensorboard. In a separate terminal, from project root, run:

```bash
tensorboard --logdir=logs/
```

If you're training from a server then you'll need to forward port 6006 to your local machine. For example, over an ssh connection you can run

```bash
ssh -N -L 6006:localhost:6006 you@server
```

And then access the tensorboard app from a local browser at localhost:6006.

To generate lyrics after training, run

```bash
python character_level_lstm/recurrent_keras.py  --mode test --weights checkpoint_layer
```

## MODEL 2

A Transformer model, which eschews recurrence in favor of the attention mechanism.

Use:
```bash
make t2t
```
to create a Docker container with tensorflow and the tensor2tensor library, and start a Jupyter Notebook from within that container. The notebook is ported out of the container on port 8889. Just as with Tensorboard, to access that port from a server forward the port using e.g.:
```bash
ssh -N -L 8889:localhost:8889 you@server
```
You should then be able to access jupyter notebook from localhost:8889 in your browser.

Follow along with the Transformer Lyric Generation notebook to train a Transformer model to generate lyrics.

Visualize the training of your model with tensorboard. In a separate terminal, from project root, run:

```bash
tensorboard --logdir=t2t_model/
```

If you're training from a server then you'll need to forward port 6006 to your local machine. For example, over an ssh connection you can run

```bash
ssh -N -L 6006:localhost:6006 you@server
```
