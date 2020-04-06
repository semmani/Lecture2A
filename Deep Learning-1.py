# Sigmoid function --> {1/(1+e^-x)}
# Tensorflow c

"""

def LinearActivationFunction(z,m):
        return m * z


def BinaryActivationFunction(z, alpha):
    return  z if z >= 0 else alpha*(e^z -10)


def ReLuActivationFunction(z):
        return 1 if z > 0 else 0

def SigmoidActivationFunction(z):
    return SigmoidActivationFunction(z) * (1 - SigmoidActivationFunction(z))

def TanhActivationFunction(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def SoftmaxActivationFunction(inputs):
        outputs = np.exp(inputs) / sum
"""


from matplotlib.pyplot as plt
import numpy as np

def sigmoid(inputs):
    outputs = []
    for x in inputs:
        result = 1/ (1 + np.exp(-x))
        outputs.append(result)

    return outputs

def main():

    inputs = list(range(0,21))
    outputs = sigmoid(inputs)
    print(inputs)
    print(outputs)

    plt.plot(inputs,outputs)
    plt.xlabel("INPUTS")
    plt.xlabel("OUTPUTS")
    plt.show()


    