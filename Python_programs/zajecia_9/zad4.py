def digit_sum(n):
    if abs(n) % 10 == n:
        return n
    else:
        return  n % 10 + digit_sum(abs(n) // 10)
print(digit_sum(11111))