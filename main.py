import pandas as pd

"Group 4 Project"


"Code: Opens a *.txt file and converts the text into a binary representation of that text."


"Decode: Opens a *.txt file with the binary codes and converts it to the characters that the binary represents."


wb = pd.read_excel("P1Dictionary.xyls", dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])

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

