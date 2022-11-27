g = int(input())
p = int(input())
enters = [0 for _ in range(g + 1)]
for i in range(p):
    max_index = int(input())
    find = False
    while not find:
        if enters[max_index] == 1:
            if max_index == 1:
                break
            max_index -= 1
        else:
            enters[max_index] = 1
            find = True

    if not find:
        print(i)
        break
