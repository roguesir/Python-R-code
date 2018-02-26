import numpy as np
import tensorflow as tf

x = [[80,3,50],[90,8,70],[180,20,120],[140,16,90]]
y = [[11],[12.5],[20],[18]]
# y = [11,12.5,20,18]
x_pred = [[120,5,85]]


tf_x = tf.placeholder(tf.float32, [None,3])     # input x
tf_y = tf.placeholder(tf.float32, [None,1])     # input y

# neural network layers
l1 = tf.layers.dense(tf_x, 20, tf.nn.relu)          # hidden layer
output = tf.layers.dense(l1, 1)                     # output layer

loss = tf.losses.mean_squared_error(tf_y, output)   # compute cost
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(loss)

sess = tf.Session()                                 # control training and others
sess.run(tf.global_variables_initializer())         # initialize var in graph


for step in range(150):
    # train and net output
    _, l, pred = sess.run([train_op, loss, output], {tf_x: x, tf_y: y})
    if step % 10 == 0:
        print('loss is: ' + str(l))
        # print('prediction is:' + str(pred))


output_pred = sess.run(output,{tf_x:x_pred})
print('input is:' + str(x_pred[0][:]))
print('output is:' + str(output_pred[0][0]))