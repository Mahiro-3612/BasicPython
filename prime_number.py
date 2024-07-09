def prime_number_checker(n):

    try:
        if not isinstance(n, int) or n < 1:
            raise ValueError("自然数ではありません")

        elif n == 1:
            return False

        elif n == 2:
            return True

        else:
            result_flag = True
            possible_factor = 2

            while possible_factor < n // 2 + 1:
                if n % possible_factor == 0:
                    result_flag = False
                    break
                else:
                    possible_factor += 1

            return result_flag
    except ValueError as e:
        return None, f"エラー: {e}"


# (1)
print(f"61は{prime_number_checker(61)}")
# (2)
print(f"10は{prime_number_checker(10)}")
# エクストラ
print(f"1.1は{prime_number_checker(1.1)}")
