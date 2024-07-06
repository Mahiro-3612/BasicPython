def prime_number_checker(input):

    if input == 1:
        return "素数ではありません"

    elif input == 2:
        return "素数です"

    else:
        possible_factor = 2

        while possible_factor < input // 2 + 1:
            if input % possible_factor == 0:
                return "素数ではありません"
                break
            else:
                possible_factor += 1

    return "素数です"


# (1)
print(f"61は{prime_number_checker(61)}")
# (2)
print(f"10は{prime_number_checker(10)}")
