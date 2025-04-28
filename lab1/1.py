import math

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
x3 = int(input('Enter x3: '))
y3 = int(input('Enter y3: '))
x4 = int(input('Enter x4: '))
y4 = int(input('Enter y4: '))

v1 = round(math.sqrt((x3 - x1)**2 + (y3 - y1)**2),3)
v2 = round(math.sqrt((x4 - x2)**2 + (y4 - y2)**2),3)

a = round(abs((x2-x1)*(y3 - y1))-((y2 - y1)*(x3 - x1)),3)


print(
    "Перша діагональ: ", v1,
    'Друга діагональ: ', v2, 
    'S: ', a,)