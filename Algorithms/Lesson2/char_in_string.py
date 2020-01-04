
our_string = input("Provide the string here: ")


def char_in_string(our_string, n):
    count = 0
    for element in our_string:
        if element == n:
            count += 1
    print(f'"{n}" in our_string is {count}')


char_in_string(our_string, n="a")
