from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM, SimpleRNN
from keras.layers.wrappers import TimeDistributed
from time import time
import argparse
from utils import *

# Take a variety of arguments for Network definition
# Provide meaningful defaults

ap = argparse.ArgumentParser()

ap.add_argument('--genre', default='rap')
ap.add_argument('--batch_size', type=int, default=50)
ap.add_argument('--layer_num', type=int, default=2)
ap.add_argument('--seq_length', type=int, default=50)
ap.add_argument('--hidden_dim', type=int, default=500)
ap.add_argument('--generate_length', type=int, default=500)
ap.add_argument('--nb_epoch', type=int, default=20)
ap.add_argument('--mode', default = 'train')
ap.add_argument('--weights', default='')
args = vars(ap.parse_args())

BATCH_SIZE = args['batch_size']
HIDDEN_DIM = args['hidden_dim']
SEQ_LENGTH = args['seq_length']
WEIGHTS = args['weights']

GENERATE_LENGTH = args['generate_length']
LAYER_NUM = args['layer_num']

GENRE = args['genre']

# Create training data
X, y, VOCAB_SIZE, ix_to_char = load_data(SEQ_LENGTH, GENRE)

print("TRAINING DATA CREATED")

#Creating network
model = Sequential()
model.add(LSTM(HIDDEN_DIM, input_shape = (None, VOCAB_SIZE), return_sequences=True))
for i in range(LAYER_NUM - 1):
    model.add(LSTM(HIDDEN_DIM, return_sequences=True))
model.add(TimeDistributed(Dense(VOCAB_SIZE)))
model.add(Activation('softmax'))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

# Generate some sample before training, which should just be noise
#generate_text(model, args['generate_length'], VOCAB_SIZE, ix_to_char)

if not WEIGHTS == '':
    model.load_weights(WEIGHTS)
    nb_epoch = 30
    #nb_epoch = int(WEIGHTS[WEIGHTS.rfind('_') + 1:WEIGHTS.find('.')])
else:
    nb_epoch = 0

# Create TensorBoard
tensorboard = TensorBoard(log_dir="logs/{}".format(time()))

# Training if there is no trained weights
if args['mode'] == 'train' or WEIGHTS == '':
    while True:
        print('\n\nEpoch: {}\n'.format(nb_epoch))
        model.fit(X, y,
                  batch_size=BATCH_SIZE,
                  verbose=1,
                  nb_epoch=1,
                  callbacks=[tensorboard])
        nb_epoch +=1
        generate_text(model, GENERATE_LENGTH, VOCAB_SIZE, ix_to_char)
        if nb_epoch % 10 == 0:
            model.save_weights('checkpoint_layer')

elif WEIGHTS == '':
    # Loading the trained weights
    model.load_weights(WEIGHTS)
    generate_text(model, GENERATE_LENGTH, VOCAB_SIZE, ix_to_char)
    print('\n\n')
else:
    print('\n\nNothing to do')
