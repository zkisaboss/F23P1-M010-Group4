import pandas as pd


file_data = pd.read_excel("F23P1-M010-Group4.xlsx", dtype=str)
chars = list(file_data["Char"])
bins = list(file_data["Bin"])


# To-Do: Support encodings with multiple characters
def encode(input_string: str) -> str:
    binary = ""
    for char in input_string:
        binary += bins[chars.index(char)]
    return binary


def decode(binary_string: str) -> str:
    output_string = ""
    binary = ""

    for bit in binary_string:
        binary += bit

        if (len(binary) == 7 and binary[0] == "1") or (len(binary) == 5 and binary[0] == "0"):
            output_string += chars[bins.index(binary)]
            binary = ""

    return output_string
