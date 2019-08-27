from __future__ import print_function, division

__author__ = 'amrit'

from keras import backend as K
import os
import importlib

## Currently using tensorflow
def set_keras_backend(backend):

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        importlib.reload(K)
        assert K.backend() == backend

#set_keras_backend("theano")


if __name__ == '__main__':
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation, Flatten
    from keras.layers.normalization import BatchNormalization
    from keras.layers import Conv2D, MaxPooling2D
    from keras.datasets import mnist
    from keras.utils import np_utils

    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test,10)


    # # import tensorflow.compat.v1 as tf
    # # tf.disable_v2_behavior()
    # model = Sequential()
    #
    # model.add(Conv2D(32, (3, 3), input_shape=(28, 28, 1)))
    # model.add(BatchNormalization(axis=-1))
    # model.add(Activation('relu'))
    # model.add(Conv2D(32, (3, 3)))
    # model.add(BatchNormalization(axis=-1))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    #
    # model.add(Conv2D(64, (3, 3)))
    # model.add(BatchNormalization(axis=-1))
    # model.add(Activation('relu'))
    # model.add(Conv2D(64, (3, 3)))
    # model.add(BatchNormalization(axis=-1))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    #
    # model.add(Flatten())
    #
    # # Fully connected layer
    # model.add(Dense(512))
    # model.add(BatchNormalization())
    # model.add(Activation('relu'))
    # model.add(Dropout(0.2))
    # model.add(Dense(10))
    #
    # model.add(Activation('softmax'))
    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    # model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

    print(y_train[0])
