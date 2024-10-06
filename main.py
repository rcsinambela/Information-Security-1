from utils.encryption import encryption
from utils.decryption import decryption
from utils.string_to_binary import str_to_bin

# Start

# user input
user_input = input("Enter a string: ")

# Encryption
enc = encryption(user_input)

# Decyption

# First convert Final Cipher text into binary
enc_to_binary = str_to_bin(enc)

# call the decryption function
dec = decryption(enc_to_binary)
