def get_middle_letters(word):
    length = len(word)
    middle = length // 2

    if length % 2 == 0:
        return word[middle-1:middle+1]
    else:
        return word[middle]

word1 = 'test'
word2 = 'testing'

print(f"Для слова '{word1}': {get_middle_letters(word1)}")
print(f"Для слова '{word2}': {get_middle_letters(word2)}")
