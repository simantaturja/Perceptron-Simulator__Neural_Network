import random
import perceptron
import point
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

lowlim, highlim = -100, 100
#plotting and animation variables
fig = plt.figure(figsize=(10, 7))
plt.suptitle('Perceptron')
ax = fig.add_subplot(121)
ax1 = fig.add_subplot(122)
ax.set_xlim(lowlim, highlim)
ax.set_ylim(lowlim, highlim)
ax1.set_xlim(lowlim, highlim)
ax1.set_ylim(lowlim, highlim)
line, = ax.plot([], [])

#Global Variables
points, animXLine, animYLine = [], [], []
a, b, c = 2, 3, 7
xLowLimit, xHighLimit, yLowLimit, yHighLimit = lowlim, highlim, lowlim, highlim
dataset = 300
brain = perceptron.Perceptron()

def pointGeneration(a, b, c):
    i = 0
    while(i <= dataset):
        tempGen = point.Point(a, b, c)
        points.append(point.Point(a, b, c))
        i = i + 1

def pointShow():
    for p in points:
        if ( p.target == 1 ):
            ax1.plot(p.x, p.y, 'go', markersize=10, markeredgecolor = 'k')
        elif ( p.target == -1 ):
            ax1.plot(p.x, p.y, 'ro', markersize=10, markeredgecolor = 'k')


def mainLine(a, b, c):
    global lineY1, lineY2
    xLine = [xLowLimit, xHighLimit]
    yLine = [a*xLowLimit+c, a*xHighLimit+c]
    ax1.plot(xLine, yLine)
    ax.plot(xLine, yLine, 'k')

def training():
    brain = perceptron.Perceptron()
    i = 0
    iteration = 1
    while( i < iteration ):
        for p in points:
            inputs = [p.x, p.y, p.bias] #bias = 1
            predict = brain.guess(inputs)

            #Getting the predicted line by the neural network
            yLow, yHigh = brain.guessLine()
            animXLine.append([xLowLimit, xHighLimit])
            animYLine.append([yLow, yHigh])

            #Train the neural network
            error = p.target - predict
            brain.train(inputs, error)
        i = i + 1

    #Training done
    for p in points:
        inputs = [p.x, p.y, p.bias] #bias = 1
        predict = brain.guess(inputs)
        if ( p.target == 1 ):
            ax.plot(p.x, p.y, 'go', label = 'correct', markersize = 10, markeredgecolor = 'k')
        else:
            ax.plot(p.x, p.y, 'ro', label = 'wrong', markersize = 10, markeredgecolor = 'k')


def userInput():
    global a, b, c
    a = int(input('Co-Efficient of x: '))
    b = int(input('Co-Efficient of y: '))
    c = int(input('Constant c: '))

def process():
    mainLine(a, b, c)
    pointGeneration(a, b, c)
    pointShow()
    training()

#Animation Functions

def init():                             #animation initializing function
    line.set_data([], [])
    return line,


def animate(i, animX, animY):           #animation update function
    print(i+1)
    line.set_data(animX[i], animY[i])
    return line,

#Animation Functions (End)


if __name__ == '__main__':
    #Take Input from Users ( Line Equation: coefficient for x, y and constant c)
    #userInput()

    #Main process starts
    process()

    #main animation function
    anim = animation.FuncAnimation(fig, animate, init_func = init, fargs=(animXLine, animYLine, ), frames = len(animXLine), interval = 1, blit = True, repeat = False)
    #anim.save("perceptron2.gif", writer=PillowWriter(fps=50)) #Saving the animation

    plt.show()
