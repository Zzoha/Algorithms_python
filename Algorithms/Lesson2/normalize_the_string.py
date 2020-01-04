crazy_string = input("Type your crazy string here. Yeh, don't forget about all the spaces everywhere: ")


def normalize(crazy_string):
    normal_string = " ".join(crazy_string.split())
    print(normal_string)


normalize(crazy_string)
