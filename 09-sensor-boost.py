import numpy as np
from collections import defaultdict

filepath = "input/temp.txt"
with open(filepath) as fp:
    line = fp.readline()
    input_program = [int(x) for x in line.split(",")]


def parameter_mode_input(mode, program, parameter_position, relative_base):
    if mode == 0:
        parameter = program[program[parameter_position]]
    elif mode == 1:
        parameter = program[parameter_position]
    elif mode == 2:
        parameter = program[program[parameter_position] + relative_base]
    else:
        raise NameError("Invalid input parameter mode")
    return parameter


def parameter_mode_output(mode, program, parameter_position, relative_base):
    if mode == 0:
        position = program[parameter_position]
    elif mode == 2:
        position = program[parameter_position] + relative_base
    else:
        raise NameError("Invalid output parameter mode")
    return position


def execute(program, input, position=0, relative_base=0):
    length = len(program)
    output = list()

    while position < length:
        instruction = program[position]
        opcode = instruction % 100

        if opcode != 99:
            mode1 = int(np.floor(instruction / 100) % 10)
            parameter1 = parameter_mode_input(
                mode1, program, position + 1, relative_base
            )

        if opcode in [1, 2, 5, 6, 7, 8]:
            mode2 = int(np.floor(instruction / 1000) % 10)
            parameter2 = parameter_mode_input(
                mode2, program, position + 2, relative_base
            )

        if opcode in [1, 2, 7, 8]:
            mode3 = int(np.floor(instruction / 10000) % 10)

        modify = -1
        instruction_length = 0

        if opcode == 1:
            modify = parameter_mode_output(mode3, program, position + 3, relative_base)
            program[modify] = parameter1 + parameter2
            instruction_length = 4
        elif opcode == 2:
            modify = parameter_mode_output(mode3, program, position + 3, relative_base)
            program[modify] = parameter1 * parameter2
            instruction_length = 4
        elif opcode == 3:
            modify = parameter_mode_output(mode1, program, position + 1, relative_base)
            if len(input) < 1:
                raise NameError("Not enough input")
            program[modify] = input.pop(0)
            instruction_length = 2
        elif opcode == 4:
            modify = -1
            output.append(parameter1)
            instruction_length = 2
        elif opcode == 5:
            if parameter1 != 0:
                position = parameter2
            else:
                instruction_length = 3
        elif opcode == 6:
            if parameter1 == 0:
                position = parameter2
            else:
                instruction_length = 3
        elif opcode == 7:
            modify = parameter_mode_output(mode3, program, position + 3, relative_base)
            if parameter1 < parameter2:
                program[modify] = 1
            else:
                program[modify] = 0
            instruction_length = 4
        elif opcode == 8:
            modify = parameter_mode_output(mode3, program, position + 3, relative_base)
            if parameter1 == parameter2:
                program[modify] = 1
            else:
                program[modify] = 0
            instruction_length = 4
        elif opcode == 9:
            relative_base += parameter1
            instruction_length = 2
        elif opcode == 99:
            pass
        else:
            raise NameError("Unkown opcode")

        if modify != position:
            position += instruction_length

        if opcode in 99:
            break
    return output


program = defaultdict(int)
for (i, j) in enumerate(input_program):
    program[i] = j
