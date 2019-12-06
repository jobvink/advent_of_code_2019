def run(operations):
    for i in range(0, len(operations), 4):
        if (i + 3) > len(operations) - 1:
            break
        o = operations[i]
        if o == 99:
            return operations

        a = operations[operations[i + 1]]
        b = operations[operations[i + 2]]
        t = operations[i + 3]
        if o == 1:
            operations[t] = (a + b)
        elif o == 2:
            operations[t] = (a * b)


    return operations


input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0'.split(',')
input = [int(i) for i in input]

for x in range(1, 99):
    for y in range(1, 99):
        test = input.copy()
        test[1] = x
        test[2] = y
        output = run(test)
        if output[0] == 19690720:
            print(x, y, (100 * x) + y)

