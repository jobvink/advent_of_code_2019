import math

values = []
with open('./input.txt', 'r') as file:
    for line in file:
        values.append(int(line))

def calc(mass):
    calculated_fule = math.floor(mass / 3) - 2
    if (calculated_fule <= 0):
        return 0
    else:
        return calculated_fule + calc(calculated_fule)


values = map(lambda x: calc(x), values)

print(sum(values))
