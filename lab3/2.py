def W_numb(string):
    n_word = 0
    in_word = False
    for char in string:
        if char != ' ' and not in_word:
            n_word += 1
            in_word = True
        elif char == ' ':
            in_word = False
    return n_word

string = input("String: ")
print(W_numb(string))
