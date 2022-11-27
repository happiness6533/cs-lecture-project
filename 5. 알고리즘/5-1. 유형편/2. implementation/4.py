def can_move(position, move):
    if move == "L":
        return True if position[0] > 1 else False
    elif move == "R":
        return True if position[0] < n else False
    elif move == "U":
        return True if position[1] > 1 else False
    else:
        return True if position[1] > n else False


if __name__ == "__main__":
    n = int(input())
    plan = input().split()

    dx = [0, 0, 1, -1]
    dy = [-1, -1, 0, 0]

    position = [1, 1]
    for move in plan:
        if move == "L":
            if can_move(position, move):
                position[1] -= 1
        elif move == "R":
            if can_move(position, move):
                position[1] += 1
        elif move == "U":
            if can_move(position, move):
                position[0] += 1
        else:
            if can_move(position, move):
                position[0] -= 1

    print(position[0], position[1])
