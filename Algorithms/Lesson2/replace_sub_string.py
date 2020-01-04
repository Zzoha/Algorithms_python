provided_string = input("Provide the string: ")
original_substring = input("Which part do you want to replace? ")
new_substring = input("With what? ")


def replace_sub_strings(orig_string, original_substring, new_substring):
    if original_substring in orig_string:
        new_string = orig_string.replace(original_substring, new_substring)
        print(new_string)
    else:
        print(f'"{original_substring}" not in the provided string. Check for spelling mistakes. Type correctly.')


replace_sub_strings(provided_string, original_substring, new_substring)
