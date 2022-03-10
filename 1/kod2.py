with open("input.txt") as text:
    lines = list(map(lambda line: int(line.rstrip()), text))


times_increased = 0

for i in range(len(lines) - 3):
    if lines[i] < lines[i + 3]:
        times_increased += 1

print(times_increased)
# 1362
