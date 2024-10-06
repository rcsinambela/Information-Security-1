def binary_to_ascii(binary_str):
    ascii_str = "".join(
        [chr(int(binary_str[i : i + 8], 2)) for i in range(0, len(binary_str), 8)]
    )
    return ascii_str
