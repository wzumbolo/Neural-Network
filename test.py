import pandas as pd
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Activation
from keras_tuner import RandomSearch
import time

LOG_DIR = f"{int(time.time())}"
d = pd.read_csv('test.csv')
D = pd.read_csv('train.csv')
df = pd.DataFrame(data=d)
df_train = pd.DataFrame(data=D)

x_test = d
y_test = d
x_train = pd.read_csv('train.csv')
y_train = [df_train.iloc[:, -1:]]
print(y_train)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)


def build_model(hp):
    model = keras.models.Sequential()

    model.add(Conv2D(hp.Int('input_units', min_value=32, max_value=256, step=32), (3, 3), input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    for i in range(hp.Int('n_layers', 1, 4)):
        model.add(Conv2D(hp.Int(f'conv_{i}_units', min_value=32, max_value=256, step=32), (3, 3)))
        model.add(Activation('relu'))

    model.add(Flatten())

    model.add(Dense(10))
    model.add(Activation("softmax"))

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    return model


tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=1,  # how many model variations to test?
    executions_per_trial=1,  # how many trials per variation? (same model could perform differently)
    directory=LOG_DIR
    )

tuner.search(x=x_train,
             y=y_train,
             # verbose=2,
             epochs=1,
             batch_size=64,
             # callbacks=[tensorboard],  # if you have callbacks like tensorboard, they go here.
             validation_data=(x_test, y_test))

print(tuner.get_best_hyperparameters()[0].values)
print(tuner.results_summary())