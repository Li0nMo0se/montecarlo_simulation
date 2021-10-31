import numpy as np
import timeit
import mc

np.random.seed(2727)    # Set the random seed
steps = 1000            # Number of small sub-steps (time)
Npaths = 10000          # Number of Monte carlo paths

S_0 = 105       # Initial stock price
K = 100         # Strike price
V_0 = 0.01      # Initial variance is square of volatility
T = 2           # time to maturity
dt = T/steps    # No. of Time step
r = 0.01

# Parameters for Heston process
variance = 0.01 # Initial variance is square of volatility
kappa = 5       # Speed of mean reversion
theta = 0.01    # Long-run variance
epsilon = 0.1   # Volatility of volatility
rho = 0.0       # Correlation


kwargs = {"steps": steps,
          "Npaths": Npaths,
          "S_0": S_0,
          "K": K,
          "V_0": V_0,
          "T": T,
          "dt": dt,
          "r": r,
          "variance": variance,
          "kappa": kappa,
          "theta": theta,
          "epsilon": epsilon,
          "rho": rho}

res_naive_mc, _, _ = mc.naive_mc(**kwargs)
res_vectorize_mc, _, _ = mc.vectorize_mc(**kwargs)

print(f"Naive MC price:     {res_naive_mc}")
print(f"Vectorize MC price: {res_vectorize_mc}")
assert np.isclose(res_naive_mc, res_vectorize_mc, atol=0.5)

NB_ITERATION = 1

t = timeit.Timer(lambda: mc.naive_mc(**kwargs))
print(f"Naive MC version:     {t.timeit(NB_ITERATION)}")

t = timeit.Timer(lambda: mc.vectorize_mc(**kwargs))
print(f"Vectorize MC version: {t.timeit(NB_ITERATION)}")
