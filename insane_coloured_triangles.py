def inc_base3(dig_n, len_n, inc_counter):
    i = 0
    while inc_counter > 0:
        if dig_n[i] < 2:
            dig_n[i] += 1
            inc_counter -= 1
            i = 0
        elif i == (len_n - 1):
            dig_n[i] = 0
            dig_n[i + 1] = 1
            len_n += 1
            inc_counter -= 1
            i = 0
        else:
            dig_n[i] = 0
            i += 1

    return len_n


def lucas_3(dig_n, dig_k):
    prod = 1
    for n_i, k_i in zip(dig_n, dig_k):
        if n_i < k_i:
            return 0
        elif n_i < 2:
            continue
        elif n_i == 2:
            if k_i == 1:
                prod = (prod * 2) % 3
        else:
            return 0
    return prod

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
    len_n = len(digits_n)

    digits_k = [0] * len_n
    len_k = 1

    i_prev = 0
    sum = 0
    for i in range(n):
        if sRGB_scheme[row[i]] > 0:
            if i > 0:
                len_k = inc_base3(digits_k, len_k, i - i_prev)
            i_prev = i
            Cnk_mod3 = lucas_3(digits_n, digits_k)
            if Cnk_mod3 > 0:
                sum = (sum + Cnk_mod3 * sRGB_scheme[row[i]]) % 3
    sign = (n % 2) * 2 - 1
    return iRGB_scheme[(3 + (sign * int(sum % 3))) % 3]