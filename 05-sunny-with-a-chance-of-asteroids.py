import numpy as np

filepath = "input/05.txt"
with open(filepath) as fp:
    line = fp.readline()
    program = [int(x) for x in line.split(",")]


def parameter_mode(mode, program, parameter_position):
    if mode == 0:
        parameter = program[program[parameter_position]]
    elif mode == 1:
        parameter = program[parameter_position]
    else:
        raise NameError("Unknown parameter mode")
    return parameter


def execute(program, input):

    position = 0
    length = len(program)
    output = list()

    while position < length:
        instruction = program[position]
        opcode = instruction % 100

        if opcode != 99:
            mode1 = int(np.floor(instruction / 100) % 10)
            parameter1 = parameter_mode(mode1, program, position + 1)

        if (
            opcode == 1
            or opcode == 2
            or opcode == 5
            or opcode == 6
            or opcode == 7
            or opcode == 8
        ):
            mode2 = int(np.floor(instruction / 1000) % 10)
            parameter2 = parameter_mode(mode2, program, position + 2)

        if opcode == 1:
            modify = program[position + 3]
            program[modify] = parameter1 + parameter2
            instruction_length = 4
        elif opcode == 2:
            modify = program[position + 3]
            program[modify] = parameter1 * parameter2
            instruction_length = 4
        elif opcode == 3:
            modify = program[position + 1]
            program[modify] = input
            instruction_length = 2
        elif opcode == 4:
            modify = -1
            output.append(parameter1)
            instruction_length = 2
        elif opcode == 5:
            modify = -1
            if parameter1 != 0:
                position = parameter2
                instruction_length = 0
            else:
                instruction_length = 3
        elif opcode == 6:
            modify = -1
            if parameter1 == 0:
                position = parameter2
                instruction_length = 0
            else:
                instruction_length = 3
        elif opcode == 7:
            modify = program[position + 3]
            if parameter1 < parameter2:
                program[modify] = 1
            else:
                program[modify] = 0
            instruction_length = 4
        elif opcode == 8:
            modify = program[position + 3]
            if parameter1 == parameter2:
                program[modify] = 1
            else:
                program[modify] = 0
            instruction_length = 4
        elif opcode == 99:
            instruction_length = 1
            break
        else:
            raise NameError("Unkown opcode")

        if modify != position:
            position += instruction_length
    return output


program_copy = program.copy()
output = execute(program, 1)
print("Part One:", output[-1])
program = program_copy.copy()
output = execute(program, 5)
print("Part Two:", output[0])
