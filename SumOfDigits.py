
#sum of digits
num = 456
n = 0
while num > 0:
    x = num % 10
    print("x", x)

    a = num // 10
    print("a", a)

    n = n + x
    print("n", n)

    num = a
    print("num", num)
print(n)

