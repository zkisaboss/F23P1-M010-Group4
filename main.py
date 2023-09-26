import pandas as pd


"""Group 4 Project"""


"""Code: Opens a *.txt file and converts the text into a binary representation of that text."""


"""Decode: Opens a *.txt file with the binary codes and converts it to the characters that the binary represents. """


"""Create python code to get the lists of binary numbers and characters from an Excel file.
        These lists should be set up such that the index for the binary value
        and its corresponding character/string value have the same list index.
        Note: When you read in the new line character from Excel, it
        becomes “\\n” instead of “\n” so you will need to fix it in your list.
        • Your character list should contain all the characters mentioned in the
        assignment as well as any strings that you also have in your Excel
        table
"""

wb = pd.read_excel("P1Dictionary.xyls", dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])

for i in range(len(bins)):
    print(bins[i], ": ", chars[i])
