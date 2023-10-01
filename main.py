import pandas as pd

xlsx = pd.read_excel("F23P1-M010-Group4.xlsx", dtype=str)
clist = list(xlsx["Char"])
blist = list(xlsx["Bin"])


# To-Do: Support encodings with multiple characters
def encode(input_string: str) -> str:
    binary = ""
    for char in input_string:
        binary += blist[clist.index(char)]
    return binary


# To-Do: Add "I" to the Excel file.
example_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .-?!'\":;,"
print(encode(example_string), len(example_string))


def decode(binary_string: str) -> str:
    output_string = ""
    binary = ""

    for bit in binary_string:
        binary += bit

        if (len(binary) == 7 and binary[0] == "1") or (len(binary) == 5 and binary[0] == "0"):
            output_string += clist[blist.index(binary)]
            binary = ""

    return output_string
