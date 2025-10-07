import math as m
import matplotlib.pyplot as plt

# Arbitrary variables
A = 1
w = 1 

xrange = [-2, -1.5, 0, 0.5, 2] # Points in space to investigate on graph - note that -2 and 2 lead to the same result

tplot = []
for i in range (m.ceil(10 * w * 2 * m.pi * 3)): # We do ten samples per unit i, and it takes 2piw seconds for one oscillation. We want three oscillations.
    tplot.append(i/10)

for x in xrange:
    y = []
    for t in tplot:
        # This equation comes directly from what I derived on the LaTeX paper
        term1 = m.pow(m.cos(x), 2) * m.exp(-1*m.pow(x,2))
        term2 = m.pow(m.sin(2*x), 2) * m.exp(-0.25*m.pow(x,2))
        term3 = 2 * m.cos(w*t) * m.cos(x) * m.sin(2*x) * m.exp(-0.625*m.pow(x,2))
        relativeProbability = 0.5 * m.pow(A, 2) * (term1 + term2 + term3) 
        y.append(relativeProbability)
    # Plot each graph of relative probability density versus time individually 
    plt.plot(tplot, y)
    plt.show()

'''
# Sanity check - We are still sloshing even if each point moves up and down at a constant frequency
trange = [0, m.pi/2, m.pi, 3*m.pi/2, 2 * m.pi] # Note the symmetry across time

xplot = []
for i in range (-10000, 10001):
    xplot.append(i/1000)
for t in range(1, 6):
    y = []
    for x in xplot:
        term1 = m.pow(m.cos(x), 2) * m.exp(-1*m.pow(x,2))
        term2 = m.pow(m.sin(2*x), 2) * m.exp(-0.25*m.pow(x,2))
        term3 = 2 * m.cos(w*t) * m.cos(x) * m.sin(2*x) * m.exp(-0.625*m.pow(x,2))
        relativeProbability = 0.5 * m.pow(A, 2) * (term1 + term2 + term3)
        y.append(relativeProbability)
    plt.plot(xplot, y)
    plt.show()
'''