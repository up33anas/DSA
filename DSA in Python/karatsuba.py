def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10 : return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a, b = divmod(x, 10 ** m)
    c, d = divmod(y, 10 ** m)

    z0 = karatsuba(b, d) # b*d
    z1 = karatsuba((a + b), (c + d)) # (a+b)*(c+d)
    z2 = karatsuba(a, c) # a*c

    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0

a = 1234
b = 5678
print(karatsuba(a, b))
print(a *b == karatsuba(a, b))