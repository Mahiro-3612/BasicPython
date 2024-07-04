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


# (1)
print(f"10と20の最大公約数は{euclid(10, 20)}")
# (2)
print(f"14と91の最大公約数は{euclid(14, 91)}")
# (3)
print(f"91と14の最大公約数は{euclid(91, 14)}")
