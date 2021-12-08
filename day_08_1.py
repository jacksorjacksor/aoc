with open("input.txt", "r") as f:
    input_received = f.read().splitlines()

dict_of_counts = {i: 0 for i in range(9)}
dict_of_letter_lengths = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


# Each line will be different
for line in input_received:
    output = line[line.find("|") + 1 :].strip()
    output_as_list = output.split(" ")
    for item in output_as_list:
        value = dict_of_letter_lengths.get(len(item))
        if value:
            dict_of_counts[value] += 1

print(sum(dict_of_counts.values()))
