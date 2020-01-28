import numpy as np

filepath='input/16.txt'
with open(filepath) as fp:
    line = fp.readline()

def convert_to_list(string):
    return [int(x) for x in string]

def convert_to_string(list):
    new_list = [str(i) for i in list]
    return''.join(new_list)

def calculate_pattern(length,position):
    base = [0,1,0,-1]
    pattern = list(np.repeat(base,position+1))
    repeat = int(np.ceil(length+1/len(pattern)))
    pattern = [x for y in range(repeat) for x in pattern]
    return pattern[1:length+1]

def fft(input):
    global pattern
    output = list()
    length = len(input)
    for i in range(length):
        result = sum(np.multiply(pattern[i], input))
        result = abs(result)%10
        output.append(result)

    return output

input = convert_to_list(line)

length = len(input)
pattern = [calculate_pattern(length,i) for i in range(length)]

for k in range(100):
    input = fft(input)
print('Part One:',convert_to_string(input)[:8])

def fft2(input):
    result = np.cumsum(input)
    result = [abs(x)%10 for x in result]
    return result

input = convert_to_list(line)
position = int(convert_to_string(input[:7]))
input = input * 10000

input.reverse()
for k in range(100):
    input = fft2(input)
input.reverse()

print('Part Two:',convert_to_string(input)[position:position+8])