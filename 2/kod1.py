with open("input.txt") as text:
    instructions = list(map(lambda line: line.rstrip().split(), text))

horizontal_position = 0
depth = 0

for instruction in instructions:
    if instruction[0] == "forward":
        horizontal_position += int(instruction[1])
    elif instruction[0] == "down":
        depth += int(instruction[1])
    else:  # => "up"
        depth -= int(instruction[1])


print(f"horizontal position: {horizontal_position}, depth: {depth}")
print(f"multiple: {horizontal_position * depth}")
# 1938402
