import pandas as pd

# Task 1: Get the lists of binary numbers and characters from an Excel file
# To-Do: Add "I" to the Excel file.
XLSX = pd.read_excel("F23P1-M010-Group4.xlsx", dtype=str)
CLIST = list(XLSX["Char"])
BLIST = list(XLSX["Bin"])


# Task 2: Create a function that returns the binary value for a given string.
def encode(string: str) -> str:
    binary = ""
    for index, value in enumerate(string):
        binary += BLIST[index]
    return binary


# Tasks 3: Write two functions that will be used to convert a binary value to a character (or string).
def decode1(binary_string: str) -> list:
    output_list = []
    binary = ""
    for bit in binary_string:
        binary += bit
        if len(binary) == 5 and binary[0] == "0" or len(binary) == 7: # appends binary to output_list when complete and resets binary to ""
            output_list.append(binary)
            binary = ""
    return output_list

def decode2(binary_char: str) -> str:
    output_list = []
    string_list = []
    string = ''
    for bit in binary_char:
        string += bit
        if (len(string) == 5 and string[0] == "0") or (len(string) == 7):
            output_list.append(string)
            string = ''
    for binary_code in output_list:
        string_list.append(clist[blist.index(binary_code)])
    return ''.join(string_list) # Join the decoded characters in 'string_list' into a single string and return it

# Step 4: Write a function that reads and creates a text file, “BinOutput.txt” that contains the binary codes.
def code(fn):
    f = open(fn, "r")
    s = f.read()
    f.close()

    binary_string = encode(s) # Call task 2 to produce a binary value
    print(binary_string)
    
    numbits = len(binary_string) # calculate num bits in the string
    binary_string = str(numbits) + "." + binary_string #update string with the bit count

    f = open("BinOutput.txt", "w+")
    f.write(binary_string)
    f.close()
    print(binary_string)

# task 5:
def decode(fn="BinOutput.txt"):
    a = open(fn, "r")
    b = a.read()
    a.close()
    i = b.index(".")
    b = b[i + 1:]
    result = ""
    while b != "":
        binary_value, b = decode1(b) # What is ,b for? 
        result = result + decode2(binary_value)
    a = open("TextOutput.txt", "w+")
    a.write(result)
    a.close()
    print(result)


# Task 6:
def compare_files(file1_name, file2_name="TextOutput.txt"):
    try:
        # Open and read the contents of the first file
        with open(file1_name, 'r') as file1:
            content1 = file1.read()

        # Open and read the contents of the second file
        with open(file2_name, 'r') as file2:
            content2 = file2.read()

        # Check if the contents of the two files are identical
        if content1 == content2:
            return True
        else:
            return False
    except FileNotFoundError:
        # Handle file not found errors
        print("One or both of the files does not exist.")
        return False
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        return False
