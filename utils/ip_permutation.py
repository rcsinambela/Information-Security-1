from utils.tables import ip_table


def ip_on_binary_rep(binary_representation):

    ip_result = [None] * 64

    for i in range(64):
        ip_result[i] = binary_representation[ip_table[i] - 1]

    # Convert the result back to a string for better visualization
    ip_result_str = "".join(ip_result)

    return ip_result_str
