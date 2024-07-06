import math


def trapezoidal_integral(func, a, b, N):

    h = (b - a) / N

    S = 0

    for k in range(1, N + 1):
        S += (h / 2) * (func(a + (k - 1) * h) + func(a + k * h))

    return S


# (問2)
print(f"求める面積は{trapezoidal_integral(math.sin, 0, math.pi / 2, 100)}")
