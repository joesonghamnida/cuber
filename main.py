word = input("Enter the word to cube: ")

def shift_letters(word):
    shifted_letters = word[1:] + word[0]
    return shifted_letters

def print_letters(word):
    i = len(word)

    while i > 0:

        if i == len(word):
            previous_value = word
        else:
            previous_value = shift_letters(word)
            word = previous_value

        print(word.upper())

        i = i - 1

print_letters(word)