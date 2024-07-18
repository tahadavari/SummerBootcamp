n = int(input())
total = (2 * n) - 1

left = 0
right = 0
center_index = 0
for i in range(n):
    if i == 0:
        center_index = (total // 2) + 1
        left = center_index - 1
        right = center_index + 1

        print((total // 2) * '.', 'D', (total // 2) * '.', sep='')
    elif i == (n - 1):
        print((total // 2) * 'D.', 'D', sep='')
    else:
        # solution 1
        # lr = (total - 2 - ((2 * i) - 1)) // 2
        # print(lr * '.', 'D', ((2 * i) - 1) * '.', 'D', lr * '.', sep='')

        # -------------------------------------------------------
        # solution 2
        for j in range(1, total + 1):
            if j == left or j == right:
                print('D', end='')
            else:
                print('.', end='')
        left -= 1
        right += 1
        print()
