def get_middle_letters(word):
    length = len(word)
    middle = length // 2

    if length % 2 == 0:
        return word[middle-1:middle+1]
    else:
        return word[middle]


word = input()
print(get_middle_letters(word))
