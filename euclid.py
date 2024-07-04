import random
import math


def euclid(a, b):

    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        while a % b != 0:
            remainder = a % b
            a = b
            b = remainder

        return b


def euclid_coprime(a, b):

    coprime_flag = False
    if euclid(a, b) == 1:
        coprime_flag = True

    return coprime_flag


def random_pairs_possibility(num_pairs=100000, min_value=1, max_value=10000):
    coprime_count = 0

    for _ in range(num_pairs):
        random1 = random.randint(min_value, max_value)
        random2 = random.randint(min_value, max_value)
        if euclid_coprime(random1, random2) is True:
            coprime_count += 1

    return coprime_count / num_pairs


# (1)
print(f"10と20の最大公約数は{euclid(10, 20)}")
# (2)
print(f"14と91の最大公約数は{euclid(14, 91)}")
# (3)
print(f"91と14の最大公約数は{euclid(91, 14)}")
# エクストラ
print(f"互いに素である確率は{random_pairs_possibility()}で、6/π^2との差は{abs(random_pairs_possibility() - 6 / math.pi ** 2)}")
