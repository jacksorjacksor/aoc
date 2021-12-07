### PART 1

from statistics import median

with open("input.txt", "r") as f:
    output = f.read()

first_array = output.split(",")

first_array_as_int = [int(i) for i in first_array]

goal = median(first_array_as_int)

list_of_distances_to_travel_to_median = []
for i in first_array_as_int:
    list_of_distances_to_travel_to_median.append(abs(i - goal))

print(list_of_distances_to_travel_to_median)
print(sum(list_of_distances_to_travel_to_median))

### PART 2

from statistics import mean

with open("input.txt", "r") as f:
    output = f.read()

first_array = output.split(",")

first_array_as_int = [int(i) for i in first_array]

goal = int(
    round(mean(first_array))
)  # THIS IS INCORRECT: ended up hard-coding the lower value - would do both the upper and lower rounding, try both and take the lower one!

list_of_distances_to_travel_to_median = []

for i in first_array_as_int:
    distance_to_travel = abs(i - goal)
    actual_amount = sum(range(int(distance_to_travel) + 1))
    list_of_distances_to_travel_to_median.append(actual_amount)

# 89791190
