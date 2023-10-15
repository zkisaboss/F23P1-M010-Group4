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
def decode1(long_binary_string: str) -> list:
    output_list = []
    binary = ""

    for bit in long_binary_string:
        binary += bit

        if len(binary) == 5 and binary[0] == "0" or len(binary) == 7:
            output_list.append(binary)
            binary = ""

    return output_list


def decode2(binary_string: str) -> str:
    return CLIST[BLIST.index(binary_string)]

# Step 4: Write a function that reads and creates a text file, “BinOutput.txt” that contains the binary codes.
def code(fn):
    f = open(fn, "r")
    s = f.read()
    f.close()

    binary_string = ''
    while x != '': #Call task 2 to produce a binary value
        binary_value, s = task_2(s)
        binary_string = binary_string + binary_value
        
    print(binary_string)
    bits = len(binary_string) # calculate num bits in the string
    binary_string = str(bits) + "." + binary_string #update string with the bit count

    f = open("BinOutput.txt", "w+")
    f.write(binary_string)
    f.close()
    print(binary_string)

# task 5:
