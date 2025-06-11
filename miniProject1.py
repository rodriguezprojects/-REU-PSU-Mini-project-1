from pylab import *

def initialize(pb0, pn0, pbn0, pnb0):

    if(not(0 <= pb0 <= 1) or not(0 <= pn0 <= 1) or pn0 + pb0 != 1
    or not(0 <= pbn0 <= 1) or not(0 <= pnb0 <= 1)):
        raise ValueError("Error values not (0 ≤ pb ≤ 1; 0 ≤ pn ≤ 1; 0 ≤ pb + pn ≤ 1)")
# Produced Error if given values are not between certain numbers
    global pb, pn, pbn, pnb, pbresult, pnresult

    pb = pb0
    pn = pn0
    pbn = pbn0
    pnb = pnb0

    pbresult = [pb]
    pnresult = [pn]

def observe():
    global pb, pn, pbresult, pnresult
    pbresult.append(pb)
    pnresult.append(pn)

def update():

    global pb, pn, pbresult, pnresult, pnb, pbn

    pbnext = pb * (1 - pbn) + (1 - pb) * pnb

    pnnext = pn * (1 - pnb) + (1 - pn) * pbn

    pb = pbnext

    pn = pnnext

initialize(0.49, 0.51, 0.95, 0.04)
for pbn0 in arange(0, 1, 0.05):
    for pnb0 in arange(0, 1, 0.05):
        initialize(0.49, 0.51, pbn0, pnb0)
        for t in range(30):
            update()
            observe()
            plot(pnresult, pbresult)

plt.plot(pnresult, 'b', label = 'Pn')
plt.plot(pbresult, 'r', label = 'Pb')
plt.title("Pb = 0.49 vs Pn = 0.51 with Pbn = 0.95 and Pnb = 0.04")
plt.legend()

show()
