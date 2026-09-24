import numpy as np

n = 120 #Number of balls

rc = 15 #Cut-off radius

l = 100 #Cube length

k = 5.0 #spring constant

r0 = 0.5 #closest distance of approach

m = np.ones((n,1)) #Mass of the balls

dt = 0.01 #time increment

t = 500 #total running time

p = np.random.uniform(0, l, size=(n, 3))

v = np.random.uniform(-1, 1, size=(n, 3))

phistory = np.zeros((t, n, 3))

# p = np.array([[-1.0, 12.0, 15.0]])
# v = np.array([[-5.0, 5.0, 5.0]])


def distpairs(p, rc):
    d = p[:, np.newaxis, :] - p[np.newaxis, :, :]

    dist = (np.sum((d**2), axis=2))**0.5

    neighbours = (dist<=rc) & (dist!=0)

    return(d, dist, neighbours)
    
def pair_forces_loop(p, rc, k, r0):
    d, dist, neighbours = distpairs(p, rc)
    f = np.zeros_like(p)
    for i in range (p.shape[0]):
        for j in range (i+1, p.shape[0]):
            if neighbours[i][j]==True:
                magnitude = -k*(dist[i][j] - r0) 
                unit_vector = d[i][j]/dist[i][j]
                force = magnitude*unit_vector
                f[i] += force
                f[j] -= force
    return(f)

def walls_reflect(p, v, l):
    for dim in range(3):
        hitp = p[:, dim] < 0
        v[hitp, dim] *= -1
        p[hitp, dim] = 0.0

        hitn = p[:, dim] > l
        v[hitn, dim] *= -1
        p[hitn, dim] = l

    return(p, v)

def step_once(p, v, m, dt, l):
    f = pair_forces_loop(p, rc, k, r0)
    a = f/m
    v += a*dt
    p += v*dt
    p, v = walls_reflect(p, v, l)
    return(p,v)

for step in range(t):
    p, v = step_once(p, v, m, dt, l)
    phistory[step] = p
    #print(p[0])


#print(phistory.shape)




p, v = walls_reflect(p, v, l)

f = pair_forces_loop(p, rc, k, r0)
np.sum(f, axis=0)

d, dist, neighbours = distpairs(p, rc)



# print(p,v)
# print(d.shape)
# print(dist.shape)
# print(neighbours.shape)
# print(p)
# print(dist)
# print(neighbours)