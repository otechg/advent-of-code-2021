with open("input.txt") as text:
    instructions = list(map(lambda line: line.rstrip().split(), text))

horizontal_position = 0
depth = 0
aim = 0

for instruction in instructions:
    if instruction[0] == "forward":
        value = int(instruction[1])
        horizontal_position += value
        depth += aim * value
    elif instruction[0] == "down":
        aim += int(instruction[1])
    else:  # => "up"
        aim -= int(instruction[1])


print(f"horizontal position: {horizontal_position}, depth: {depth}")
print(f"multiple: {horizontal_position * depth}")
