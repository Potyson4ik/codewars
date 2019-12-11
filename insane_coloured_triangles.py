sRGB_scheme = {'R': 0, 'G': 1, 'B': 2}
iRGB_scheme = {0: 'R', 1: 'G', 2: 'B'}

def int_base_number(number, base_number):
    while number > 0:
        yield number % base_number
        number = number // base_number

def triangle(row):
    n = len(row)

    number = n - 1
    digits_n = list(int_base_number(number, 3))

    sum = 0
    for i in range(n):
        if sRGB_scheme[row[i]] > 0:
            number = i
            Cnk_mod3 = 1
            for digit_n in digits_n:
                digit_k = number % 3
                number = number // 3
                if digit_n == 2 and digit_k == 1:
                    Cnk_mod3 = 2 if Cnk_mod3 == 1 else 1
                elif digit_k > digit_n or digit_n > 2:
                    Cnk_mod3 = 0
                    break
            if Cnk_mod3 > 0:
                sum = (sum + Cnk_mod3 * sRGB_scheme[row[i]]) % 3
    sign = (n % 2) * 2 - 1
    return iRGB_scheme[(3 + (sign * int(sum % 3))) % 3]
