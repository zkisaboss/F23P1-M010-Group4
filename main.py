import pandas as pd

# Task 1: Get the lists of binary numbers and characters from an Excel file
# To-Do: Add "I" to the Excel file.
XLSX = pd.read_excel("F23P1-M010-Group4.xlsx", dtype=str)
CLIST = list(XLSX["Char"])
BLIST = list(XLSX["Bin"])


# Task 2: Create a function that returns the binary value for a given string.
def encode(string_input: str) -> str:
    binary = ""
    for index, value in enumerate(string_input):
        binary += BLIST[index]
    return binary


# Tasks 3: Write two functions that will be used to convert a binary value to a character (or string).
def decode_part1(long_binary_string: str) -> list:
    output_list = []
    binary = ""

    for bit in long_binary_string:
        binary += bit

        if len(binary) == 5 and binary[0] == "0" or len(binary) == 7:
            output_list.append(binary)
            binary = ""

    return output_list


def decode_part2(binary_string: str) -> str:
    return CLIST[BLIST.index(binary_string)]

# Step 4: Write a function that reads and creates a text file, “BinOutput.txt” that contains the binary codes.
