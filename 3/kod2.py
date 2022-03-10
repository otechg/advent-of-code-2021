def bit_criteria_filter(list_to_sort, pos, rare_mode=False):
    if len(list_to_sort) == 1:
        return list_to_sort

    bit_0 = []
    bit_1 = []

    for num in list_to_sort:
        if num[pos] == "1":
            bit_1.append(num)
        else:
            bit_0.append(num)

    if rare_mode:
        # co2
        return bit_1 if len(bit_1) < len(bit_0) else bit_0
    else:
        # oxygen
        return bit_0 if len(bit_0) > len(bit_1) else bit_1


with open("input.txt") as input:
    numbers = input.read().split("\n")

line_length = len(numbers[0])

oxygen_rating = numbers
co2_rating = numbers
for i in range(line_length):
    oxygen_rating = bit_criteria_filter(oxygen_rating, i)
    co2_rating = bit_criteria_filter(co2_rating, i, rare_mode=True)


final_number = int(oxygen_rating[0], 2) * int(co2_rating[0], 2)
# 2795310

# nápad na optimalizaci: v první fázi třízení stačí projít seznam jednou a rozházet jej do dvou skupin
