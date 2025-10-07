import math as m

A = 1
x = 1 # change to vary over time
w = 1 # change to be realistic 
t = 1 # change to be variable

term1 = m.pow(m.cos(x), 2) * m.exp(-1*m.pow(x,2))
term2 = m.pow(m.sin(2*x), 2) * m.exp(-0.25*m.pow(x,2))
term3 = 2 * m.cos(w*t) * m.cos(x) * m.sin(2*x) * m.exp(-0.625*m.pow(x,2))

relativeProbability = 0.5 * m.pow(A, 2) * (term1 + term2 + term3)
print(relativeProbability)