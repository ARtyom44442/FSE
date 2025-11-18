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


def search(seq, endcoded_seq):
    decoded = decode_rle(endcoded_seq)
    if seq in decoded:
        return True
    else:
        return False

def diff(first_chain, second_chain):
    decoded_first = decode_rle(first_chain)
    decoded_second = decode_rle(second_chain)

    difference_count =abs(len(decoded_first) - len(decoded_second))

    max_len = max(len(decoded_first), len(decoded_second))
    for i in range(max_len):
        char_first = decoded_first[i] if i < len(decoded_first) else None
        char_second = decoded_second[i] if i < len(decoded_second) else None
        if char_first != char_second:
            difference_count += 1

    return difference_count


def mode(chain):
    decoded_chain = decode_rle(chain)
    replay = {}

    for char in decoded_chain:
        replay[char] = replay.get(char, 0) + 1
    max_char = None
    max_count = -1

    for char, count in replay.items():
        if count > max_count:
            max_char = char
            max_count = count

    print(max_char, "\t\t\t", max_count)