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

    if increasing and adjecency:
        return True
    else:
        return False

output = 0
for i in range(246515, 739105):
    if check(i):
        output += 1

print(output)