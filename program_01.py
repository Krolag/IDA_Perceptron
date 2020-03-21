import matplotlib.pyplot as plt
from random import random, seed
from numpy import array, append, linspace

# Seed for ranomization, so the experiment could be redone
seed(2)

# Function for randomizing input vectors
def randVector(n, flag):
    tmp = []
    for i in range(n):
        if flag == True and i == 0:
            tmp.append(1)
        else:
            value = random() * 10 - 5
            tmp.append(value)
    return array(tmp)

x = randVector(100, False)
y = randVector(100, False)

# Writing [x, y] points to the *.txt
f = open("values.txt", "w+")
cattegory = []
for i in range(len(x)):
    if y[i] > (2 * x[i] - 2): # y = 2x - 2
        cattegory.append(1)
    else:
        cattegory.append(0)

    if (i < 99):
        f.write(str(x[i]) + " " + str(y[i]) + " " + str(cattegory[i]) + "\n")
    else:
        f.write(str(x[i]) + " " + str(y[i]) + " " + str(cattegory[i]))
f.close()
