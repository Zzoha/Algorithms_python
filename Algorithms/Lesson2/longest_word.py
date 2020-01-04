word_string = input("Provide the string: ")


def longest_word(word_string):
    words = word_string.split(", ")
    long_word = max(words, key=len)
    print(f'Count of letters in the longest word "{long_word}" is: {len(long_word)}')


longest_word(word_string)
