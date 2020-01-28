filepath = "input/02.txt"
with open(filepath) as fp:
    line = fp.readline()
    program = [int(x) for x in line.split(",")]


def step(program, position):
    opcode = program[position]
    first = program[position + 1]
    second = program[position + 2]
    third = program[position + 3]

    length = len(program)

    if opcode == 1:
        if first >= length or second >= length or third >= length:
            return -1
        program[third] = program[first] + program[second]
    elif opcode == 2:
        if first >= length or second >= length or third >= length:
            return -1
        program[third] = program[first] * program[second]

    return opcode


def execute(program):
    position = 0
    returncode = 1
    while returncode == 1 or returncode == 2:
        returncode = step(program, position)
        position = position + 4
    return returncode


program_copy = program.copy()

program[1] = 12
program[2] = 2
returncode = execute(program)
print("Part One:", program[0])


def find_noun_verb(program_copy):
    length = len(program_copy)
    for noun in range(100):
        for verb in range(100):
            program = program_copy.copy()
            program[1] = noun
            program[2] = verb
            returncode = execute(program)
            if program[0] == 19690720 and returncode == 99:
                return 100 * noun + verb


print("Part Two:", find_noun_verb(program_copy))
