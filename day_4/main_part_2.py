# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

start_range = 246515
end_range = 739105


def check(i):
    digits = str(i)
    increasing = False
    highest = 0
    # determine whether digets increase
    for c in digits:
        if int(c) >= highest:
            highest = int(c)
            increasing = True
        else:
            return False

    adjecency = False
    for i, c in enumerate(digits):
        if i + 1 < len(digits):
            if c == digits[i + 1]:
                adjecency = True

    if not increasing or not adjecency:
        return False

    # determines if the groups contains ajecent chars of 2 but nog more
    # e.g. 123444 is not in group
    # (1 2), (2 3), (3 4), (4 4), (4, 4)
    current = 0
    twoAjecent = False
    for i, c in enumerate(digits):
        if i + 1 < len(digits):
            next = int(digits[i + 1])
            if twoAjecent and int(c) > current:
                return True
            elif int(c) == next and int(c) == current:
                twoAjecent = False
            elif int(c) == next and not twoAjecent:
                current = int(c)
                twoAjecent = True


    return twoAjecent

print(check(111111))
print(check(223450))
print(check(123789))
print(check(112233))
print(check(123444))
print(check(111122))

output = 0
for i in range(246515, 739105):
    if check(i):
        output += 1

print(output)

