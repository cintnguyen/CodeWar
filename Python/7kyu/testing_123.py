# 7 kyu
# Testing 1-2-3
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]


def number(lines):
    arr = []
    i = 1
    for v in lines:
        if v == "":
            arr.append(f"{i}: {v}")   
            i = i + 1
        else:
            arr.append(f"{i}: {v}")
            i = i + 1
    return arr