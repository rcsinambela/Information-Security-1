def str_to_bin(user_input):

    # Convert the string to binary
    binary_representation = ""

    for char in user_input:
        # Get ASCII value of the character and convert it to binary
        binary_char = format(ord(char), "08b")
        binary_representation += binary_char
        binary_representation = binary_representation[:64]

    # Pad or truncate the binary representation to 64 bits
    binary_representation = binary_representation[:64].ljust(64, "0")

    # Print the binary representation
    # print("Binary representation of input string: ", binary_representation)
    # print(len(binary_representation), 'bits of input string')

    return binary_representation
