count = 0
minimum = 372304
maximum = 847060

for i in range(3,10):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                for m in range (l,10):
                    for n in range(m,10):
                        integer = int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))
                        if (i==j or j==k or k==l or l==m or m==n) and integer>=minimum and integer<=maximum:
                            count+=1 

print('Part One:',count)

def adjacent_matching(i,j,k,l,m,n):
    if i==j and j!=k:
        return True
    elif i!=j and j==k and k!=l:
        return True
    elif j!=k and k==l and l!=m:
        return True
    elif k!=l and l==m and m!=n:
        return True
    elif l!=m and m==n:
        return True
    else:
        return False

count = 0
for i in range(3,10):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                for m in range (l,10):
                    for n in range(m,10):
                        integer = int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))
                        if adjacent_matching(i,j,k,l,m,n) and integer>=minimum and integer<=maximum:
                            count+=1 

print('Part Two:',count)