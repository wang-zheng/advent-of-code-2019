import numpy as np
import itertools

filepath = "input/07.txt"
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


def execute(program, input, position=0):
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
            if len(input) < 1:
                raise NameError("Not enough input")
            program[modify] = input.pop(0)
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
            instruction_length = 0
        else:
            raise NameError("Unkown opcode")

        if modify != position:
            position += instruction_length

        if opcode == 4 or opcode == 99:
            break
    return output, position


max_result = -99999
max_phases = [-1 - 1 - 1 - 1 - 1]

perm = itertools.permutations([0, 1, 2, 3, 4])
for permutation in list(perm):
    output, position = execute(program.copy(), [permutation[0], 0])
    output, position = execute(program.copy(), [permutation[1], output[0]])
    output, position = execute(program.copy(), [permutation[2], output[0]])
    output, position = execute(program.copy(), [permutation[3], output[0]])
    output, position = execute(program.copy(), [permutation[4], output[0]])
    result = output[0]
    if result > max_result:
        max_result = result
        max_phases = permutation

print("Part One:", max_result)

max_result = -99999
max_phases = [-1 - 1 - 1 - 1 - 1]

perm = itertools.permutations([5, 6, 7, 8, 9])
for permutation in list(perm):
    programA = program.copy()
    programB = program.copy()
    programC = program.copy()
    programD = program.copy()
    programE = program.copy()
    positionA = 0
    positionB = 0
    positionC = 0
    positionD = 0
    positionE = 0
    output, positionA = execute(programA, [permutation[0], 0], position=positionA)
    output, positionB = execute(
        programB, [permutation[1], output[0]], position=positionB
    )
    output, positionC = execute(
        programC, [permutation[2], output[0]], position=positionC
    )
    output, positionD = execute(
        programD, [permutation[3], output[0]], position=positionD
    )
    output, positionE = execute(
        programE, [permutation[4], output[0]], position=positionE
    )
    while programE[positionE] != 99:
        output, positionA = execute(programA, output, position=positionA)
        output, positionB = execute(programB, output, position=positionB)
        output, positionC = execute(programC, output, position=positionC)
        output, positionD = execute(programD, output, position=positionD)
        output, positionE = execute(programE, output, position=positionE)
        if len(output) == 1:
            result = output[0]
    if result > max_result:
        max_result = result
        max_phases = permutation

print("Part Two:", max_result)
