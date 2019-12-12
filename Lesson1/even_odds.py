def even_odd(num):
    num_str = str(num)
    print("Count of even:", sum(dig.isdigit() for dig in num_str if int(dig) % 2 == 0))
    print("Count of odds:", sum(dig.isdigit() for dig in num_str if int(dig) % 2 != 0))


even_odd(28535873291950375)
