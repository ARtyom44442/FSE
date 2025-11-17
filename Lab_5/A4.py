def decode_rle(sequence):
    decoded = []
    i = 0
    while i < len(sequence):
        if sequence[i].isdigit():
            count = int(sequence[i])
            char = sequence[i + 1]
            decoded.append(char * count)
            i += 2
        else:
            decoded.append(sequence[i])
            i += 1
    return ''.join(decoded)