def Fibo(n):
    a = 0
    b = 1
    c = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n):
            a, b = b, a+b
            c.append(b)
        return (b, c)

n = int(input('Enter n:'))
print(Fibo(n))
