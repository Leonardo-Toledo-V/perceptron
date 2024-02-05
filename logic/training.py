import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from logic.graphics import graphic

class Perceptron:
    def __init__(self,eta, weight, X, Y):
        self.eta = eta
        self.weight = weight
        self.X = X
        self.Y = Y

weights = []
err=[]

def functionStep(x):
    return 1 if x >= 0 else 0

def initialization(data):
    column = data.csv_read.shape[1]
    Y = data.csv_read.iloc[:, column-1]
    X = data.csv_read.iloc[:,0: column-1]
    X.insert(0, "x0", 1)
    weights = [round(w, 2) for w in np.random.uniform(-1, 1, column)]
    Y = Y.to_numpy().reshape(-1, 1)
    X = X.to_numpy()
    weights = np.array(weights).reshape(1, -1)
    neuron = Perceptron(data.eta,weights, X, Y)
    cycle(neuron, data.epoch)

def cycle(neuron, epoch):
    for i in range(epoch):
        training(neuron)
    graphic(weights, err)
    err.clear()
    weights.clear()

def training(neuron):
    U = np.linalg.multi_dot([neuron.X, neuron.weight.T])
    y_C = np.vectorize(functionStep)(U)
    error = neuron.Y - y_C
    change_weights = neuron.eta * np.dot(error.T, neuron.X)
    neuron.weight = neuron.weight + change_weights
    norma_error = np.linalg.norm(error)    
    weights.append(np.squeeze(neuron.weight))
    err.append(norma_error)