matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]
]

current_index_i = 1
current_index_j = 0

n = input()


def is_death(ii, jj):
    if ii > 1 or jj > 7 or ii < 0 or jj < 0:
        return True
    return False


for i in n:
    if i == "F":
        current_index_j += 1
        if is_death(current_index_i, current_index_j):
            print("DEATH")
            break
        matrix[current_index_i][current_index_j] = 1

    elif i == "L":
        current_index_i -= 1
        current_index_j += 1
        if is_death(current_index_i, current_index_j):
            print("DEATH")
            break
        matrix[current_index_i][current_index_j] = 1

    elif i == "R":
        current_index_i += 1
        current_index_j += 1
        if is_death(current_index_i, current_index_j):
            print("DEATH")
            break
        matrix[current_index_i][current_index_j] = 1
else:
    print(*matrix[0], sep='')
    print(*matrix[1], sep='')
