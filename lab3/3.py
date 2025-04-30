def generate_subsets(char_set):
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

s = input('Ns:')
print(generate_subsets(s))
