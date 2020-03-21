import matplotlib.pyplot as plt
from random import random, seed
from numpy import array, append, genfromtxt
from program_01 import randVector

def activationFunction(u):
    if u > 0:
        return 1
    if u <= 0:
        return 0

# Reading the input values from the *.txt file
trainingInput = genfromtxt("values.txt")

# Randomizing values of the weights
w = randVector(3, True)
print("Random weights before learning:")
print(w)

# Step factor value
eta = 0.1

# Transforming the trainingInput values into three different arrays
x1 = [] # x
x2 = [] # y
xdraw1 = []
xdraw2 = []
ydraw1 = []
ydraw2 = []
trainingOutput = [] # category
for i in range(len(trainingInput)):
    x1.append(trainingInput[i][0])
    x2.append(trainingInput[i][1])
    trainingOutput.append(trainingInput[i][2])

for i in range(len(trainingInput)):
    if (trainingInput[i][2] == 0):
        xdraw1.append(trainingInput[i][0])
        ydraw1.append(trainingInput[i][1])
    else:
        xdraw2.append(trainingInput[i][0])
        ydraw2.append(trainingInput[i][1])

f = open("SynapticWeights.txt", "w+")

tmp = array([])
# Training part of the neural network
for iterator in range(100):
    for i in range(len(x1)):

        linearFunction = array([])
        output = x1[i] * w[1] + x2[i] * w[2] + w[0] # y-vector
        fu = activationFunction(output)

        for j in range(len(x2)):
            linearFunction = append(linearFunction, (-w[0] / w[2]) - (w[1] * x1[j] / w[2]))
        
        if iterator == 0 and i == 0 or iterator == 1 and i == 0 or iterator == 99 and i == 0:
            plt.xlim(-5, 5)
            plt.ylim(-5, 5)
            plt.plot(xdraw1, ydraw1, 'o', xdraw2, ydraw2, '^', x1, linearFunction)
            plt.show()
            if (iterator == 99):
                f.write(str(w[1]) + ' ' + str(w[2]) + ' ' + str(w[0]))
            else:
                f.write(str(w[1]) + ' ' + str(w[2]) + ' ' + str(w[0]) + '\n')
        
        if (fu > trainingInput[i][2]):
            w = w - array([w[0], x1[i], x2[i]]) * eta
        if (fu < trainingInput[i][2]):
            w = w + array([w[0], x1[i], x2[i]]) * eta
        else:
            pass

f.close()