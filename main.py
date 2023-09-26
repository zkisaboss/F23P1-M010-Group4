import pandas as pd

"Group 4 Project"


"Encode: Opens a *.txt file and converts the text into a binary representation of that text."


def encoder(string: str) -> str:
    file = pd.read_excel("NAME_THIS_FILE.xlsx", dtype=str)
    bins = list(file["Bin"])
    chars = list(file["Char"])

    for i in range(len(bins)):
        print(bins[i], ": ", chars[i])

    # Open File
    text_output = open("TextOutput.txt")
    s1 = text_output.read()
    print(s1)
    text_output.close()

    bin_output = open("BinOutput.txt")
    s2 = bin_output.read()
    print(s2)
    bin_output.close()
    
    binary = ""
    for i in range(len(chars)):
        binary = binary + bins[i]
    
    return binary


"Decode: Opens a *.txt file with the binary codes and converts it to the characters that the binary represents."


def decoder():
    pass
