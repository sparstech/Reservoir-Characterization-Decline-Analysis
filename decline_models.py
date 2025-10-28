
import numpy as np
def arps_rate(qi, d, b, t):
    if b == 0:
        return qi * np.exp(-d * t)
    else:
        return qi / ((1 + b * d * t)**(1.0 / b))

def compute_eur(qi, d, b, t_max=1000):
    ts = np.arange(0, t_max+1)
    rates = arps_rate(qi, d, b, ts)
    return np.sum(rates)
