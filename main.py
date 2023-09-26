import pandas as pd

"Group 4 Project"


"Encode: Opens a *.txt file and converts the text into a binary representation of that text."


def encoder(excel_file: str):
    file = pd.read_excel(excel_file, dtype=str)
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


"Decode: Opens a *.txt file with the binary codes and converts it to the characters that the binary represents."


def decoder():
    pass
