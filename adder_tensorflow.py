from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np

# Inputs and outputs
A = np.array([
    [1, 2],
    [1, 3],
    [1, 1],
    [3, 3]
])
b = np.array([3, 4, 2, 6])

# Creating the model
# Use learning_rate = 0.1 or not it is too slow
# Use SGD (Stochastic Gradient Descent) as an optimizer and MSE as a metric because this is not a classification but a regression problem
x = Input(shape=(2,))
y = Dense(1, activation="linear")(x)
model = Model(x, y)
optimizer = SGD(learning_rate=0.1)
model.compile(loss="mse", optimizer=optimizer, metrics=["mse"])

# Fitting the model
model.fit(A, b, epochs=30)

# Getting model weights
w_array = model.layers[1].get_weights()[0]
print("[w1, w2] = [{:.2f}, {:.2f}]".format(w_array[0][0], w_array[1][0]))
