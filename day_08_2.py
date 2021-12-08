with open("input.txt", "r") as f:
    input_received = f.read().splitlines()


dict_of_simple_lengths_to_numbers = {
    # length: number
    2: 1,  # simple
    4: 4,  # simple
    3: 7,  # simple
    7: 8,  # simple
}

list_of_numbers_to_bars_needed = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
]

sum = 0

for line in input_received:
    output = line[line.find("|") + 1 :].strip()
    output_to_decode = output.split(" ")
    print(f"{output_to_decode=}")

    dict_of_letter_combinations = {i: "" for i in range(9)}

    dict_of_def_line_assignments = {i: None for i in range(7)}

    list_to_work_out = []

    # We now want the 10 chars BEFORE the line
    output = line[: line.find("|")].strip()
    output_as_list = output.split(" ")
    for item in output_as_list:
        simple_number = dict_of_simple_lengths_to_numbers.get(len(item))
        if simple_number:
            dict_of_letter_combinations[simple_number] += item
            dict_of_letter_combinations[simple_number] = "".join(
                list(set([i for i in dict_of_letter_combinations[simple_number]]))
            )
        else:
            list_to_work_out.append(item)

    dict_of_letter_combinations[5] = [
        item for item in list_to_work_out if len(item) == 5
    ]
    dict_of_letter_combinations[6] = [
        item for item in list_to_work_out if len(item) == 6
    ]

    ############################################
    # location [0]: the value in 7 that isn't in 1
    for letter in dict_of_letter_combinations[7]:
        if letter not in dict_of_letter_combinations[1]:
            dict_of_def_line_assignments[0] = letter

    ############################################
    # location [6]
    # Find 9
    for item in dict_of_letter_combinations[6]:
        contains_four = True
        for char in dict_of_letter_combinations[4]:
            if char not in item:
                contains_four = False
        if contains_four:
            string_of_9 = item
            # Find the letter which is not in FOUR or [0]
            for letter in string_of_9:
                if (
                    letter not in dict_of_letter_combinations[4]
                    and letter not in dict_of_def_line_assignments[0]
                ):
                    dict_of_def_line_assignments[6] = letter

    ############################################
    # location [4]
    """
    9 is only 6 character number that contains all elements of 4
    Can use this to determine [4]
    """

    for item in dict_of_letter_combinations[6]:
        test = True
        for four_char_letter in dict_of_letter_combinations[4]:
            if four_char_letter not in item:
                test = False
        if test:
            # We've found 9
            string_of_9 = item
            # [4] is only character of 9 one NOT in 8
            for character in dict_of_letter_combinations[8]:
                if character not in string_of_9:
                    dict_of_def_line_assignments[4] = character
    # for number in six_character_numbers:

    ############################################
    # location [2]
    # location [5]
    """
    of the numbers with 5 characters
    ONLY 2 does have [4]
    2 is the only 5 character number with [5]
    Therefore we can prove [5] 
    """
    for item in dict_of_letter_combinations[5]:
        finder_of_4 = False
        for character in item:
            if character == dict_of_def_line_assignments[4]:
                finder_of_4 = True
        if finder_of_4:
            string_of_2 = item
            # We can prove [5]
            # number 1 has [2] and [5].
            # number 2 has [2] not [5]
            for letter in dict_of_letter_combinations[1]:
                if letter not in string_of_2:
                    dict_of_def_line_assignments[5] = letter
                else:
                    dict_of_def_line_assignments[2] = letter

    ############################################
    ### 3
    # location [3]
    # find THREE by checking all 5 digit numbers and checking that they contain both digits of ONE
    for item in dict_of_letter_combinations[5]:
        check = True
        for letter in dict_of_letter_combinations[1]:
            if letter not in item:
                check = False
        if check:
            string_of_3 = item
            for char in string_of_3:
                if char not in dict_of_def_line_assignments.values():
                    dict_of_def_line_assignments[3] = char
    # Then check which value isn't already stored. That value is [3]

    # location [1]
    ## 3 is the only 5 character number which contains both [2] and [5]
    ## From this we can work out position [3] as we already have values for the other [characters]
    for item in dict_of_letter_combinations[8]:
        if item not in dict_of_def_line_assignments.values():
            dict_of_def_line_assignments[1] = item

    # swap around the dict
    dict_of_letters_to_numbers = {
        value: key for key, value in dict_of_def_line_assignments.items()
    }

    eventual_value = ""
    # THEN use the INPUT to establish the OUTPUT
    for value in output_to_decode:
        actual_number = []
        for char in value:
            actual_number.append(dict_of_letters_to_numbers[char])
        actual_number.sort()
        # Sort, then check
        for index, bar_representation in enumerate(list_of_numbers_to_bars_needed):
            if bar_representation == actual_number:
                eventual_value += str(index)
    sum += int(eventual_value)

print(f"{sum=}")
