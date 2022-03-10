with open("input.txt") as text:
    numbers = text.read().split("\n")

count_of_1 = [0] * len(numbers[0])

for number in numbers:
    for i, char in enumerate(number):
        if char == "1":
            count_of_1[i] += 1

result = ""
result_inverted = ""
half_of_lines = len(numbers) / 2
for count in count_of_1:
    if count >= half_of_lines:
        result += "1"
        result_inverted += "0"
    else:
        result += "0"
        result_inverted += "1"

final_number = int(result, 2) * int(result_inverted, 2)
# 3148794
