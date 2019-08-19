import random

#Global Variables
lowlim, highlim = -100, 100
learningRate = 0.1
xLowLimit, xHighLimit, yLowLimit, yHighLimit = lowlim, highlim, lowlim, highlim

def activation(sum):
    if ( sum >= 0 ):
        return 1
    else:
        return -1

class Perceptron:
    weights = []
    def __init__(self):
        for i in range(3):
            self.weights.append(random.uniform(-1, 1))

    def guess(self, inputs):
        sum = 0.0
        for i in range(3):
            sum += inputs[i] * self.weights[i];
        return activation(sum)

    def train(self, inputs, error):
        for i in range(3):
            self.weights[i] += inputs[i] * error * learningRate

    def guessLine(self):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]
        yLow = -(w2 / w1) - (w0 / w1) * xLowLimit
        yHigh = -(w2 / w1) - (w0 / w1) * xHighLimit
        return yLow, yHigh
