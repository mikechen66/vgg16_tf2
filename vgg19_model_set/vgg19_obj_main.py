#!/usr/bin/env python
# coding: utf-8

# vgg19_Obj_main.py

"""
It is the OOP style VGG19 model including a  main function that works as the code of 
the scaffolding. 

Very Deep Convolutional Networks for Large-Scale Image Recognition
ICLR 2015: https://arxiv.org/abs/1409.1556

Keras code: 
https://github.com/keras-team/keras-applications/blob/master/keras_applications/vgg16.py

Tensorflow code:  
https://github.com/tensorflow/models/blob/master/research/slim/nets/vgg.py
"""


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D


# Define the vgg19 model 
class Vgg19(Sequential):

    def __init__(self, input_shape, num_classes):
        super().__init__()

        # Conv Block 1 
        self.add(Conv2D(filters=64, kernel_size=(3,3), padding="same", activation="relu", input_shape=input_shape))
        self.add(Conv2D(filters=64, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

        # Conv Block 2 
        self.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

        # Conv Block 3 
        self.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

        # Conv Block 4 
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

        # Conv Block 5 
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

        # FC Layer 6~8 
        self.add(Flatten())
        self.add(Dense(units=4096, activation="relu"))
        self.add(Dense(units=4096, activation="relu"))
        self.add(Dense(units=num_classes, activation="softmax"))


if __name__ == '__main__':

    IMAGE_WIDTH = 227
    IMAGE_HEIGHT = 227
    CHANNELS = 3
    NUM_CLASSES = 1000

    # Assign the vlaues 
    INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS)

    # Call the Vgg19 model 
    model = Vgg19(INPUT_SHAPE, NUM_CLASSES)

    # show the full model structure of the Vgg19 
    model.summary()
