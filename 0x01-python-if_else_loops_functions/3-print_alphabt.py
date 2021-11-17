#!/usr/bin/python3
for lower in range(97, 123):
    if lower not in [101, 113]:
        print("{}".format(chr(lower)), end="")
