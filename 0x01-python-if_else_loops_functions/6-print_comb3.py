#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical."""

for digitOne in range(0, 10):
    for digitTwo in range(digitOne + 1, 10):
        if digitOne == 8 and digitTwo == 9:
            print("{}{}".format(digitOne, digitTwo))
        else:
            print("{}{}".format(digitOne, digitTwo), end=", ")
