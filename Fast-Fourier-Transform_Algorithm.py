import numpy as np

def fft(x):
    n = len(x)
    if n == 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    t = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + t[:n//2] * odd,
                           even + t[n//2:] * odd])

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])

print(fft(x))
