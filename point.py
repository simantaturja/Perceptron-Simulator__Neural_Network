import random
lowlim, highlim = -100, 100
xLowLimit, xHighLimit, yLowLimit, yHighLimit = lowlim, highlim, lowlim, highlim


class Point:
    x = y = 0.0
    target = 0
    bias = 1
    def __init__(self, a, b, c):
        self.x = random.uniform(xLowLimit, xHighLimit)
        self.y = random.uniform(yLowLimit, yHighLimit)
        lineY = a * self.x + c
        #lineY = random.uniform(a*xLowLimit+c, a*xHighLimit+c)
        #gp = getPosition(xLowLimit, a*xLowLimit+c, xHighLimit, a*xHighLimit+c, self.x, self.y)
        gp = self.y > lineY
        if ( gp == 1 ):
            self.target = 1
        elif ( gp == 0 ):
            self.target = -1
