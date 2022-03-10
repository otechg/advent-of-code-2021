with open("input.txt") as text:
    numbers = text.read()

count_of_1 = [0] * numbers.find("\n")

index = 0
for char in numbers:
    if char == "1":
        count_of_1[index] += 1
        index += 1
    elif char == "\n":
        index = 0
    else:  # "0"
        index += 1

result = ""
result_inverted = ""
half_of_lines = numbers.count("\n") / 2
for num in count_of_1:
    if num >= half_of_lines:
        result += "1"
        result_inverted += "0"
    else:
        result += "0"
        result_inverted += "1"

final_number = int(result, 2) * int(result_inverted, 2)
print(final_number)
# 3148794
