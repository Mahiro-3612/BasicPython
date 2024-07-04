import math


def trapezoidal_integral(f, a=0, b=1, n=100):

    h = (b - a) / n

    S = 0

    for k in range(1, n + 1):
        S += (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))

    return S


def func2(x):
    return 4 / (1 + x ** 2)


def func3(x):
    return math.sqrt(math.pi) * math.exp(-x ** 2)


# (制御構文問2)
print(f"求める面積は{trapezoidal_integral(math.sin, 0, math.pi / 2, 100)}")

# 関数問2(1)
print(f"求める面積は{trapezoidal_integral(func2, 0, 1, 100)}")

# 関数問2(2)
print(f"求める面積は{trapezoidal_integral(func3, -100, 100, 1000)}")
