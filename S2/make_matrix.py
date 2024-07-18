i = int(input())
j = int(input())

matrix = [[0 for jj in range(j)] for ii in range(i)]

for ii in range(i):
    print(*matrix[ii])
