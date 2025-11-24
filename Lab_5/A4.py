import sys

with open('genedata.0.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f


    def decode_rle(sequence):
        decoded = []
        i = 0
        while i < len(sequence):
            if sequence[i].isdigit():
                j = i
                while j < len(sequence) and sequence[j].isdigit():
                    j += 1
                count = int(sequence[i:j])
                char = sequence[j]
                decoded.append(char * count)
                i = j + 1
            else:
                decoded.append(sequence[i])
                i += 1
        return ''.join(decoded)


    protein = []
    creature = []
    chains = []

    with open("sequences.0.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                protein.append(parts[0])
                creature.append(parts[1])
                chains.append(parts[2])

    proteins_chains = dict(zip(protein, chains))


    def search(pattern, encoded_seq):
        decoded_pattern = decode_rle(pattern)
        decoded_seq = decode_rle(encoded_seq)
        return decoded_pattern in decoded_seq


    def diff(first_chain, second_chain):
        decoded_first = decode_rle(first_chain)
        decoded_second = decode_rle(second_chain)

        difference_count = abs(len(decoded_first) - len(decoded_second))

        max_len = min(len(decoded_first), len(decoded_second))
        for i in range(max_len):
            if decoded_first[i] != decoded_second[i]:
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

        print(f"{max_char}\t\t\t{max_count}")


    with open("commands.0.txt", "r", encoding="utf-8") as file:
        print("-" * 60)
        count_command = 0
        for line in file:
            command = line.strip().split("\t")

            if command[0] == "search":
                count_command += 1
                dec_pattern = decode_rle(command[1])
                print(f"{count_command:03d}\tsearch\t{dec_pattern}")
                print("{:<12}    {:>15}".format("organism", "protein"))

                found = False
                for i in range(len(protein)):
                    if search(command[1], chains[i]):
                        print("{:<12}    {:<25}".format(creature[i], protein[i]))
                        found = True

                if not found:
                    print("NOT FOUND")
                print("-" * 60)

            elif command[0] == "diff":
                count_command += 1
                print(f"{count_command:03d}\tdiff\t{command[1]}\t{command[2]}")
                print("amino-acids difference:")
                if command[1] in proteins_chains and command[2] in proteins_chains:
                    result = diff(proteins_chains[command[1]], proteins_chains[command[2]])
                    print(result)
                else:
                    print("Protein not found")
                print("-" * 60)

            elif command[0] == "mode":
                count_command += 1
                print(f"{count_command:03d}\tmode\t{command[1]}")
                print("amino-acids occurs:")
                if command[1] in proteins_chains:
                    mode(proteins_chains[command[1]])
                else:
                    print("Protein not found")
                print("-" * 60)
