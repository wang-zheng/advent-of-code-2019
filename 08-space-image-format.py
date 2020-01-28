filepath='input/08.txt'

with open(filepath) as fp:
    line = fp.readline()
    arr = [int(c) for c in line]

wide =25
tall =6
deep =int(len(arr)/wide/tall)

picture = [[[0 for k in range(wide)] for j in range(tall)] for i in range(deep)]
c = 0
for i in range(deep):
    for j in range(tall):    
        for k in range(wide):
            picture[i][j][k] = arr[c]
            c += 1

def get_layer(i):
    layer = [c for row in picture[i] for c in row] 
    return layer

min_layer = get_layer(0)
min_zeros = 9999999
for i in range(deep):
    layer = get_layer(i)
    zeros = layer.count(0)
    if zeros < min_zeros:
        min_zeros = zeros
        min_layer = layer

print('Part One:',min_layer.count(1)*min_layer.count(2))

final_image = [[-1 for k in range(wide)] for j in range(tall)]
for j in range(tall):
    for k in range(wide):
        for i in range(deep):
            c = picture[i][j][k]
            if c != 2:
                final_image[j][k] = c
                break

print('Part Two:')
for j in range(tall):
    for k in range(wide):
        if final_image[j][k] == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print('',end='\n')