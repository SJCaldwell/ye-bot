# ye-bot
RNN that takes in character level rap lyrics and puts out BARS. 

## Usage
Download lyrics to data folder

```bash
python3 lyric_scraping/lyric_scrape.py
```

spin up docker container, which automatically mounts this repository

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

