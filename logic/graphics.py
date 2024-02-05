import matplotlib.pyplot as plt
import numpy as np

def graphic(weights, err):
    fig, axes = plt.subplots(figsize=(8, 6))
    we = np.array(weights)
    iterations = list(range(1, len(we) + 1))
    for i in range(we.shape[1]):
        axes.plot(iterations, we[:, i], label=f'w{i}', linestyle="-")
    axes.set_title('Evolución de pesos por generación')
    plt.xlabel('Iteración')
    plt.ylabel('Valor del Peso')
    plt.legend()
    plt.savefig("weights-evolution.jpg")
    plt.show()
    plt.close(fig)
    #siguiente grafica 
    errors = np.array(err)
    fig, axes = plt.subplots(figsize=(8, 6))
    for i in range(we.shape[1]):
        axes.plot(iterations, errors, linestyle="-")
    axes.set_title('Evolución del error')
    axes.set_xlabel('Iteración')
    axes.set_ylabel('Error')
    plt.savefig("error-evolution.jpg")
    plt.show()
    plt.close(fig)
