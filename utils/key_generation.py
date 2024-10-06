from utils.key_conversion import key_in_binary_conv
from utils.tables import pc1_table
from utils.tables import pc2_table
from utils.tables import shift_schedule


def generate_round_keys():

    # Key into binary
    binary_representation_key = key_in_binary_conv()
    pc1_key_str = "".join(binary_representation_key[bit - 1] for bit in pc1_table)

    # Split the 56-bit key into two 28-bit halves
    c0 = pc1_key_str[:28]
    d0 = pc1_key_str[28:]
    round_keys = []
    for round_num in range(16):
        # Perform left circular shift on C and D
        c0 = c0[shift_schedule[round_num] :] + c0[: shift_schedule[round_num]]
        d0 = d0[shift_schedule[round_num] :] + d0[: shift_schedule[round_num]]
        # Concatenate C and D
        cd_concatenated = c0 + d0

        # Apply the PC2 permutation
        round_key = "".join(cd_concatenated[bit - 1] for bit in pc2_table)

        # Store the round key
        round_keys.append(round_key)
    return round_keys
