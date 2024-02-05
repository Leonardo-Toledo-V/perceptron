import numpy as np
import tkinter as tk
from logic.graphics import plot_error_evolution, plot_weights_evolution

class Perceptron:
    def __init__(self,eta, weight, X, Y):
        self.eta = eta
        self.weight = weight
        self.X = X
        self.Y = Y    
    def functionStep(x):
        return 1 if x >= 0 else 0

weights = []
err=[]

def initialization(data):
    num_columns = data.csv_read.shape[1]
    Y = data.csv_read.iloc[:, -1].to_numpy().reshape(-1, 1)
    X = data.csv_read.iloc[:,0: num_columns-1]
    X.insert(0, "x0", 1)
    X = X.to_numpy()
    weights = np.array( [round(w, 2) for w in np.random.uniform(-1, 1, num_columns)]).reshape(1, -1)
    neuron = Perceptron(data.eta,weights, X, Y)
    cycle(neuron, data.epoch)

def cycle(neuron, epoch):
    for i in range(epoch):
        training(neuron)
    plot_weights_evolution(weights)
    plot_error_evolution(err)
    err.clear()
    weights.clear()

def training(neuron):
    U = np.dot(neuron.X, neuron.weight.T)
    y_C = np.vectorize(Perceptron.functionStep)(U)
    error = neuron.Y - y_C
    newWeights = neuron.eta * np.dot(error.T, neuron.X)
    neuron.weight = neuron.weight + newWeights
    normaError = np.linalg.norm(error)    
    weights.append(neuron.weight.flatten().tolist())
    err.append(normaError)