def key_in_binary_conv():
    # Original key (can be changed but it should be 8 char)
    original_key = "abcdefgh"
    binary_representation_key = ""

    for char in original_key:
        # Convert the characters to binary and concatenate to form a 64-bit binary string
        binary_key = format(ord(char), "08b")
        binary_representation_key += binary_key

    return binary_representation_key
