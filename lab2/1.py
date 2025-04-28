S = list()
S = [4, -5, 15, 1, 20, 4, -8, 35]
S.sort(reverse=True)

Suma = 0

for i in range(5):
    k = S[i]**3
    Suma += k

print('Сума кубів 5 найбільших елементів: ', Suma)
