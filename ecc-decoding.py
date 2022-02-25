import numpy as np
import csv

# parity check matrix
H = np.array([
    [1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 1]
])

col_indices = range(1, 9)

# read messages in CSV
messages = csv.reader(open('message.csv'))
msg = ""

for row in messages:
    # convert each row to a vector
    y = np.array([int(i) for i in row])

    # calculate syndrome
    syndrome = np.matmul(H, y) % 2

    # find bit number to flip
    bit_num = -1
    for i, col in zip(col_indices, H.T):
        if (col == syndrome).all(): bit_num = i

    # flip the corrupt bit
    if bit_num in col_indices:
        y[bit_num-1] = (y[bit_num-1] + 1) % 2

    # trim 9-bit vector to 5 bits
    y = y[:5]

    # convert 5-bit string to decimal representation
    char_num = int("".join(str(x) for x in y), 2)

    # convert decimal to letter
    letter = ' ' if char_num == 0 else chr(char_num + 64)

    # add letter to string
    msg += letter

print("Decoded message: " + msg)