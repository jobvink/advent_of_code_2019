class program:
    def __init__(self, opcodes):
        self.memory = list(opcodes)
        self.pointer = 0
        self.halt = False
        self.output = []

    def next(self, parameter_length=1):
        data = self.memory[self.pointer:self.pointer + parameter_length]
        self.pointer += parameter_length
        return data

    def param_values(self, op: int, parameter_length: int) -> list:
        arguments = list(self.next(parameter_length))
        modes = []
        op = op // 100
        for i in range(len(arguments)):
            modes.append(op % 10)
            op = op // 10

        parameters = []
        for value, mode in zip(arguments, modes):
            if mode == 0:
                parameters.append(self.memory[value])
            elif mode == 1:
                parameters.append(value)

        return parameters

    def step(self):
        instr, = self.next()
        op = instr % 100

        if op == 1:
            a, b = self.param_values(instr, 2)
            res_loc, = self.next()

            self.memory[res_loc] = a + b

        elif op == 2:
            a, b = self.param_values(instr, 2)
            res_loc, = self.next()

            self.memory[res_loc] = a * b

        elif op == 3:
            addr, = self.next()
            input_value = input('diagnostic code: ')

            self.memory[addr] = int(input_value)

        elif op == 4:
            value, = self.param_values(instr, 1)
            self.output.append(value)

        elif op == 5:
            cond, jump_addr = self.param_values(instr, 2)
            if cond:
                self.pointer = jump_addr

        elif op == 6:
            cond, jump_addr = self.param_values(instr, 2)
            if not cond:
                self.pointer = jump_addr

        elif op == 7:
            x, y = self.param_values(instr, 2)
            addr, = self.next()

            self.memory[addr] = int(x < y)

        elif op == 8:
            x, y = self.param_values(instr, 2)
            addr, = self.next()

            self.memory[addr] = int(x == y)

        elif op == 99:
            self.halt = True

        else:
            self.halt = True

    def run(self):
        while not self.halt:
            self.step()

        return self.output


file = open('./input.txt')
memory = [int(x) for x in file.readline().split(',')]
file.close()
p = program(memory)
print(p.run())
