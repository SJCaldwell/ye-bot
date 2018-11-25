# ye-bot
RNN that takes in character level rap lyrics and puts out BARS. 

Follows [Combining Learned Lyrical Structures and Vocabulary for Improved Lyric Generation](https://arxiv.org/pdf/1811.04651.pdf#cite.vaswani17attention)

## Usage
First refer to the data/README, and download or supply any data you wish to use.

Then spin up a docker container, which automatically mounts this repository

```bash
sudo make bash
```

train model

```bash
python3 modeling/recurrent_keras.py
```

visualize training with tensorboard. In a separate terminal, from project root, run:

```bash
./start_tensorboard.sh
```

validate and test model

```bash

```

