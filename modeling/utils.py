import os
import numpy as np

DATA_DIR = "../data/"

def create_corpus_for_genre(genre):
    """Create a corpus based off of lyrics in a whole genre.
    If the genre does not exist, return an empty string.
    
    Arguments:
        genre {string} -- Genre description - e.g rap, pop
    
    Returns:
        string -- Entire corpus concatenated together.
    """
    corpus = ""
    if genre in os.listdir(DATA_DIR):
        #iterate through artists
        for artist in os.listdir(DATA_DIR + "/" + genre + "/"):
            for filename in os.listdir(DATA_DIR + "/" + genre + "/" + artist + "/"):
                with open(DATA_DIR + "/" + genre + "/" + artist + "/" + filename) as f:
                    corpus += f.read()
    return corpus


def create_corpus_for_artist(artist):
    """Create a corpus based off of lyrics for a specific artist.
    If the artist does not exist, return an empty string.
    
    Arguments:
        artist {string} -- name of artist - e.g kanyewest, ladygaga
    
    Returns:
        string -- Entire corpus concatenated together
    """
    raise NotImplementedError

def load_data(seq_length, genre="rap"):
    data = create_corpus_for_genre(genre)
    chars = list(set(data))
    VOCAB_SIZE = len(chars)

    print('Data Length: {} characters'.format(len(data)))
    print('Vocabulary Size: {} characters'.format(VOCAB_SIZE))

    ix_to_char = {ix:char for ix, char in enumerate(chars)}
    char_to_ix = {char:ix for ix, char in enumerate(chars)}

    X = np.zeros((len(data)/seq_length, seq_length, VOCAB_SIZE))
    y = np.zeros((len(data)/seq_length, seq_length, VOCAB_SIZE))

    for i in range(0, len(data)/seq_length):
        X_sequence = data[i * seq_length: (i+1)*seq_length]
        X_sequence_ix = [char_to_ix[value] for value in X_sequence]
        input_sequence = np.zeros((seq_length, VOCAB_SIZE))
        for j in range(seq_length):
            input_sequence[j][X_sequence_ix[j]] = 1.0
            X[i] = input_sequence
        
        y_sequence = data[i*seq_length+1:(i+1)*seq_length+1]
        y_sequence_ix = [char_to_ix[value] for value in y_sequence]
        target_sequence = np.zeros((seq_length, VOCAB_SIZE))
        for j in range(seq_length):
            target_sequence[j][y_sequence_ix[j]] = 1.0
            y[i] = target_sequence
    return X, y, VOCAB_SIZE, ix_to_char

def generate_text(model, length, vocab_size, ix_to_char):
    # starting with random character
    ix = [np.random.randint(vocab_size)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, vocab_size))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)

if __name__ == "__main__":
    print (create_corpus_for_genre("rap"))
    create_corpus_for_genre("techno")
