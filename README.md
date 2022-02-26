# Montecarlo simulation benchmarks

## Heston model

$S_{t+1}= S_{t}e^{(r-\frac{V_t}{2})dt + \sqrt{V_t}dW_{t}}$

$V_{t+1} = V_{t} + \kappa(\theta - V_{t})dt + \xi\sqrt{V_t}dW_{t}$

## Usage

* Install virtual enviornment

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

* Run benchmarks

```shell
python bench.py
```
possible output:
```
Naive MC price:     9.929162911882436
Vectorize MC price: 9.709896276684509
Naive MC version:     88.22001631200055
Vectorize MC version: 1.1054078840006696
```
