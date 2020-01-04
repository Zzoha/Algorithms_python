string1 = input("Provide first word: ")
string2 = input("Provide second word: ")


def anagram_check(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()

    if string1 == string2 or len(string1) != len(string2):
        return "Word is not an anagram"
    for char in string1:
        if string1.count(char) != string2.count(char):
            return "Word is not an anagram"
    return "Word is an anagram"


print(anagram_check(string1, string2))
