n = int(input('Enter in range from 1 to 100:'))
attempts = int(input('Number of attempts:'))
a = []
all = []
for x in range(attempts):
    str_inp = input('Numbers: ')
    answer = list(map(int, str_inp.split()))
    len_answr = len(answer)
    for number in answer:
        all.append(number)
    if n in answer:
        print('Yes')
    else:
        print('No')    
help = input('Need help?(if yes, print HELP. Else just 0):')
if help == 'HELP':
    print(all)
else:
    print('You lose :p')


