with open("input.txt", "r") as file:
    list_of_fish = file.readlines()[0].split(",")

cycle_of_old_fish = 6
cycle_of_new_fish = 8
day_counter = 0
max_day_counter = 80

fish_dictionary = {i: 0 for i in range(9)}

for fish in list_of_fish:
    fish_dictionary[int(fish)] += 1

for i in range(256):
    result_store = {i: 0 for i in range(9)}
    for i in range(9):
        fish_amount = fish_dictionary[i]
        if i == 0:
            result_store[6] += fish_amount
            result_store[8] += fish_amount
        else:
            result_store[i - 1] += fish_amount
    fish_dictionary = {key: value for key, value in result_store.items()}

output = sum(fish_dictionary.values())
