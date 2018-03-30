# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""
import numpy as np 
np.random.seed(1337)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers import Dense,Activation,Convolution2D,MaxPooling2D,Flatten
from keras.optimizers import Adam


(X_train,y_train),(X_test,y_test)=mnist.load_data()


X_train = X_train.reshape(-1,1,28,28)
X_test = X_test,reshape(-1,1,28,28)
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)


# Another way to build CNN
model=Sequential()


# Conv layer 1 output shape (32,28,28)
model.add(Convolution2D(
	nb_filter=32,
	nb_row=5,
	nb_col=5,
	border_mode='same',    # padding method
	input_shape=(1,28,28),
	))

model.add(Activation('relu'))

# Pooling layer 1 (max pooling) output shape (32,14,14)
model.add(MaxPooling2D(
	pool_size=(2,2),
	strides=(2,2),
	border_mode='same',
	))

# Conv layer 2 output shape (64,14,14)
model.add(Convolution2D(64,5,5,border_mode='same'))
model.add(Activation('relu'))

# Pooling layer 2 (max pooling) output shape (64,7,7)
model.add(MaxPooling2D(pool_size=(2,2),border_mode='same'))


# Fully connected layer 1 input shape (64*7*7)=(3136)
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

# Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(10))
model.add(Activation('softmax'))

# Another way to define your optimizer
adam = Adam(lr=1e-4)

# We add metrics to get more results you want to see
model.compile(optimizer=adam,
			loss='categorical_crossentropy',
			metrics=['accuracy'])

print('Training----------')
# Another way to train the model
model.fit(X_train,y_train,nb_epoch=1,batch_size=32,)

print('Testing----------')
loss,accuracy = model.evaluate(X_test,y_test)

print('\ntest loss:',loss)
print('\naccyracy:',accuracy)














