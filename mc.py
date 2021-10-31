import numpy as np
import matplotlib.pyplot as plt
from typing import *

def vectorize_mc(steps: int,
                 Npaths: int,
                 S_0: float,
                 K: float,
                 V_0: float,
                 T: float,
                 dt: float,
                 r: float,
                 variance: float,
                 kappa: float,
                 theta: float,
                 epsilon: float,
                 rho: float) -> Tuple[float, np.array, np.array]:

    V_t = np.empty((Npaths,steps))
    S_t = np.empty((Npaths,steps))
    V_t[:,0] = V_0
    S_t[:,0] = S_0
    for t in range(1,steps):
        # Random numbers for S_t and V_t
        W_t =  np.random.multivariate_normal(mean = np.array([0,0]),
        				cov = np.array([[1,rho],
        						[rho,1]]),
        					size=Npaths)

        # Euler integration
        V_t[:,t-1] = np.maximum(V_t[:,t-1], 0)
        S_t[:,t] = S_t[:,t-1] * np.exp( np.sqrt(V_t[:,t-1] * dt) * W_t[:,0] + (r - V_t[:,t-1]/2) * dt)                     # Stock price process
        V_t[:,t] = np.abs(V_t[:,t-1] + kappa * (theta - V_t[:,t-1]) * dt + epsilon * np.sqrt(V_t[:,t-1] * dt) * W_t[:,1]) 

    price = np.mean(np.maximum(S_t[:,-1]-K,0))*np.exp(-r*T)
    return price, S_t, V_t


def naive_mc(steps: int,
             Npaths: int,
             S_0: float,
             K: float,
             V_0: float,
             T: float,
             dt: float,
             r: float,
             variance: float,
             kappa: float,
             theta: float,
             epsilon: float,
             rho: float) -> Tuple[float, np.array, np.array]:
    V = np.empty((Npaths,steps))
    S = np.empty((Npaths,steps))
    for n in range(Npaths):
        V[n,0] = V_0
        S[n,0] = S_0
        # Random numbers for S_t and V_t
        W =  np.random.multivariate_normal(mean = np.array([0,0]),
    				cov = np.array([[1,rho],
    						[rho,1]]),
    				size=steps)
        for t in range(1,steps):
            # Euler integration
            V[n,t-1] = np.maximum(V[n,t-1], 0)
            S[n,t] = S[n,t-1] * np.exp(np.sqrt(V[n,t-1] * dt) * W[t,0] + (r - V[n,t-1]/2) * dt)
            V[n,t] = np.abs(V[n,t-1] + kappa * (theta - V[n,t-1]) * dt + epsilon * np.sqrt(V[n,t-1] * dt) * W[t,1])

    price = np.mean(np.maximum(S[:,-1]-K,0))*np.exp(-r*T)
    return price, S, V