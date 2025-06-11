from pylab import *

def initialize(pb0, pn0):

    if(pb0 > 1 or pn0 > 1 or pb0 < 0 or pn0 < 0 or pn0 + pb0 > 1 or pn0 + pb0 < 0):
        raise ValueError("Error values not (0 ≤ pb ≤ 1; 0 ≤ pn ≤ 1; 0 ≤ pb + pn ≤ 1)")
# Produced Error if given values are not between certain numbers
    global pb, pn, pbresult, pnresult

    pb = pb0
    pn = pn0

    pbresult = [pb]
    pnresult = [pn]

def observe():
    global pb, pn, pbresult, pnresultg
    pbresult.append(pb)
    pnresult.append(pn)

def update():

    global pb, pn, pbresult, pnresultg

    nextx = 0.5 * x + y
    nexty = -0.5 * x + y
    x, y = nextx, nexty

for x0 in arange(0, 1, 0.5):
    for y0 in arange(-2, 2, 0.5):
        initialize(x0, y0)
        for t in range(30):
            update()
            observe()
        plot(xresult, yresult, 'b')

show()
