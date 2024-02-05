import matplotlib.pyplot as plt
import numpy as np

def plot_weights_evolution(weights, save_filename="WeightsEvolution.jpg"):
    fig, axes = plt.subplots(figsize=(8, 6))
    iterations = list(range(1, len(weights) + 1))
    weights_array = np.array(weights)
    for i in range(weights_array.shape[1]):
        axes.plot(iterations, weights_array[:, i], label=f'w{i}', linestyle="-")
    axes.set_title('Evolución de pesos por generación')
    axes.set_xlabel('Iteración')
    axes.set_ylabel('Valor del Peso')
    axes.legend()
    plt.savefig(save_filename)
    plt.show()
    plt.close(fig)

def plot_error_evolution(errors, save_filename="ErrorEvolution.jpg"):
    fig, axes = plt.subplots(figsize=(8, 6))
    iterations = list(range(1, len(errors) + 1))
    axes.plot(iterations, errors, linestyle="-" ,c="red")
    axes.set_title('Evolución del error')
    axes.set_xlabel('Iteración')
    axes.set_ylabel('Error')
    plt.savefig(save_filename)
    plt.show()
    plt.close(fig)
