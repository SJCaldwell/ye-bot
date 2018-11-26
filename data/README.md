[Combining Learned Lyrical Structures and Vocabulary for Improved Lyric Generation](https://arxiv.org/pdf/1811.04651.pdf#cite.vaswani17attention)

The structure folder contains lyrics text data across different genres, which will be used to train a lyric structure model on the syntactic structure of songs. Use scrape_genius_lyrics.py to automatically scrape artist lyrics from Genius, a lyric-hosting website. Specify what artists you want to scrape using artists.csv.

The vocabulary folder is used for training the Lyric vocabulary model, and can use any text corpus you want. To use the same data as in the paper, go [here](https://www.kaggle.com/currie32/project-gutenbergs-top-20-books/version/1), create a Kaggle account if you don't already have one, and extract the rtf files into the vocabulary folder.
