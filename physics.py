import numpy as np
from variables import *


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

def step_once(p, v, m, dt, l, rc, k, r0):
    f = pair_forces_loop(p, rc, k, r0)
    a = f/m
    v += a*dt
    p += v*dt
    p, v = walls_reflect(p, v, l)

    return(p,v)

def run_simulation(p, v, m, t, dt, l, rc, k, r0):
    phistory = np.zeros((t, p.shape[0], 3))
    for step in range(t):
        p, v = step_once(p, v, m, dt, l, rc, k, r0)
        phistory[step] = p

    return(phistory)