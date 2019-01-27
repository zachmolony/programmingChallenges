# machine learning

import numpy as np
#import matplotlib.pyplot as plt
from random import randint

# input data
x_data = [1.0, 2.0, 3.0]

# expected output data
y_data = [2.0, 4.0, 6.0]

# random weight
w = float(randint(0,10))


def feedForward(x):
    return x * w


def lossError(x,y):
    return (feedForward(x) - y)**2


def computeGradient(x, y):
    return 2 * x * (x*w-y)


x = x_data[0]
y = y_data[0]
lossError(x,y)

# Training the AI

#setting the learning rate
alpha = 0.1

#how many interations does it take to change the weight
for epoch in range(1,101):
    for x, y in zip(x_data, y_data):
        gradient = computeGradient(x, y)

        #update weight
        w = w - 0.01 * gradient #experiment eith
        loss = lossError(x, y)
        print("x: {}, weight: {}, loss: {}".format(epoch, w, loss))
        print("------------------------------------"); print("")

print("before training, 4 hours spent studying is predited to get {} points".format(feedForward(4)))


# Generated weight algorithm below
all_weights = []
all_mses = []


for w in np.arange(0.0, 4.1, 0.1):
    print("w=", w)
    sum_of_all_loss = 0
    for x, y in zip(x_data, y_data):
        hypothesis_x = feedForward(x)
        loss = lossError(x, y)
        sum_of_all_loss += loss
        print("x:", x)
        print("y:", y)
        print("hypothesis x (y):", hypothesis_x)
        print("loss/error squared for this weight {}".format(w), loss)
        print("")
    print("MSE: ", loss/3); print("")
    print("----------------------------------")
    all_weights.append(w)
    all_mses.append(loss/3)


#plt.title("loss vs weights")
#plt.plot(all_weights, all_mses)
#plt.ylabel("loss")
#plt.xlabel("weights")
#plt.show()
