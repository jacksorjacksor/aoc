# input format: 0,9 -> 5,9

with open("AoC/day_05/input.txt", "r") as f:
    file_input = f.read().splitlines()

# Define classes
class InputPoint:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self) -> str:
        return f"InputPoint ({self.x1},{self.y1} -> {self.x2},{self.y2})"


class GridPoint:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.count_of_found = 0

    def __repr__(self) -> str:
        return f"GridPoint ({self.x},{self.y} - count: {self.count_of_found} | found by: {self.found_by})"


# 1. split the file_input into a list of classes:
# [{x1:0, y1:0, x2:0, y2:0}

list_of_input_points = [
    InputPoint(
        int(line[0 : line.find(",")]),
        int(line[line.find(",") + 1 : line.find(" -> ")]),
        int(line[line.find(" -> ") + 4 : line.find(",", line.find(" -> "))]),
        int(line[line.find(",", line.find(" -> ")) + 1 :]),
    )
    for line in file_input
]


# 2. decide how big the grid is.
max_x = max(
    [point.x1 for point in list_of_input_points]
    + [point.x2 for point in list_of_input_points]
)
max_y = max(
    [point.y1 for point in list_of_input_points]
    + [point.y2 for point in list_of_input_points]
)

# list_of_grid_points = [
#     GridPoint(x, y) for x in range(max_x + 1) for y in range(max_y + 1)
# ]
# print(f"{len(list_of_grid_points)=}")

# 4. go over each point, count the instances an InputPoint crosses over a GridPoint.
# --- When crossed, += GridPoint.count_of_found
list_of_grid_points = []
counter = 0
for input_point in list_of_input_points:
    print(counter)
    # print(f"Input point: {input_point}")

    # straight line check
    if input_point.x1 == input_point.x2 or input_point.y1 == input_point.y2:
        if input_point.y1 == input_point.y2:
            x_inc, x2_mod = (1, 1) if input_point.x1 < input_point.x2 else (-1, -1)
            x_range = range(input_point.x1, input_point.x2 + x2_mod, x_inc)
            y_range = range(input_point.y1, input_point.y1 + 1)
        else:
            y_inc, y2_mod = (1, 1) if input_point.y1 < input_point.y2 else (-1, -1)
            y_range = range(input_point.y1, input_point.y2 + y2_mod, y_inc)
            x_range = range(input_point.x1, input_point.x1 + 1)

        for x in x_range:
            for y in y_range:
                try:
                    grid_point = [
                        grid_point
                        for grid_point in list_of_grid_points
                        if (grid_point.x, grid_point.y) == (x, y)
                    ][0]
                    grid_point.count_of_found += 1
                except:
                    list_of_grid_points.append(GridPoint(x, y))
                    # print(f"Found: {grid_point}")

    # diagonal line check
    else:
        # calc the ranges correctly
        x_inc, x2_mod = (1, 1) if input_point.x1 < input_point.x2 else (-1, -1)
        y_inc, y2_mod = (1, 1) if input_point.y1 < input_point.y2 else (-1, -1)
        x_range = range(input_point.x1, input_point.x2 + x2_mod, x_inc)
        y_range = range(input_point.y1, input_point.y2 + y2_mod, y_inc)
        for x, y in zip(x_range, y_range):
            try:
                grid_point = [
                    grid_point
                    for grid_point in list_of_grid_points
                    if (grid_point.x, grid_point.y) == (x, y)
                ][0]
                grid_point.count_of_found += 1
            except:
                list_of_grid_points.append(GridPoint(x, y))

    # print(" * ")
    counter += 1

list_of_grid_points_with_count_of_found_over_0 = [
    grid_point for grid_point in list_of_grid_points if grid_point.count_of_found > 0
]

print(f"{len(list_of_grid_points_with_count_of_found_over_0)}")
# for i in list_of_grid_points_with_count_of_found_over_0:
#     print(i)

# missing: (3,4 && 7,4)
