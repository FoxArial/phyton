m = int(input('Enter m: '))

div = []
for i in range(1, m+1):
    if m%i == 0:
        div.append(i)
print('Дільники', m, ': ', div)
