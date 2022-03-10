from timeit import timeit

# code = """
with open("input.txt") as input:
    numbers = input.read().split("\\n")

bits_1 = []
bits_0 = []
for num in numbers:
    if num[0] == "1":
        bits_1.append(num)
    else:
        bits_0.append(num)

if len(bits_1) > len(bits_0):
    oxygen_rating = bits_1


# """

# print(timeit(code, number=20000))
