def fast_pow(base, exp):
    if exp < 0:
        return 0
    elif exp == 0:
        return 1
    if exp % 2 == 0:
        return fast_pow(base*base, exp//2)
    else:
        return base * fast_pow(base, exp - 1)
print(fast_pow(1012, 2))
