with open("input.txt") as text:
    lines = list(map(lambda line: int(line.rstrip()), text))


times_increased = 0
previous_line = lines[0]

for line in lines:
    if line > previous_line:
        times_increased += 1
    previous_line = line


print(times_increased)
# 1387
