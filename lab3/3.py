def generate_subsets(k):
    char_set = k.split()
    n = len(char_set)
    subsets = []

    for i in range(2**n):
        subset = ''
        for j in range(n):
            if (i >> j) & 1:
                subset += char_set[j]
        subsets.append(subset)

    for s in subsets:
       print(s)

inp = input('Введіть символи через пробіл: ')
generate_subsets(inp)
