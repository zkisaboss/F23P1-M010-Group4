import pandas as pd


def load_file(file_path: str) -> tuple:
    """
    Load an Excel file containing character & binary mappings.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        tuple: A tuple containing two lists, one for characters and one for binary representations.
    """
    # Load the Excel file
    file = pd.read_excel(file_path, dtype=str)
    chars = list(file["Char"])
    bins = list(file["Bin"])
    return chars, bins


# Load the data from the Excel file
chars, bins = load_file("F23P1-M010-Group4.xlsx")


def encode(input_string: str) -> str:
    """
    Encode a text string into its binary representation.

    Args:
        input_string (str): The input text to encode.

    Returns:
        str: The binary representation of the input text.
    """
    binary = ""
    for char in input_string:
        binary += bins[chars.index(char)]
    return binary


# Call the encode function with an example input
encoded_text = encode("My name is James.")
print(encoded_text)


def decode(binary_string: str) -> str:
    """
    Decode a binary string into its corresponding characters.

    Args:
        binary_string (str): The binary string to decode.

    Returns:
        str: The decoded text.
    """
    decoded_text = ""
    binary = ""

    for bit in binary_string:
        binary += bit

        if (len(binary) == 7 and binary[0] == "1") or (len(binary) == 5 and binary[0] == "0"):
            decoded_text += chars[bins.index(binary)]
            binary = ""

    return decoded_text


# Decode the encoded text
decoded_text = decode(encoded_text)
print(decoded_text)
