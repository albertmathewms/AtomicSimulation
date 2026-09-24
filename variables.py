import numpy as np

n = 12 #Number of balls

rc = 3 #Cut-off radius

l = 10 #Cube length

k = 5.0 #spring constant

r0 = 0.5 #closest distance of approach

m = np.ones((n,1)) #Mass of the balls

dt = 0.01 #time increment

t = 500 #total running time

p = np.random.uniform(0, l, size=(n, 3))

v = np.random.uniform(-50, 50, size=(n, 3))
