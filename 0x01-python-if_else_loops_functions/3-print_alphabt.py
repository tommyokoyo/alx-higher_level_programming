#!/usr/bin/python3
for i in range(97, 123):
    if i == "q" and i == "e":
        continue
    else:
        print("{}".format(chr(i)), end = "")
