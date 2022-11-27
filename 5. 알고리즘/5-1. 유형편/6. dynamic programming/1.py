x = int(input())


def calculation(x, array, candidates, count):
    candidates[f"{count}"] = []
    if count == 1:
        if (x * 5) not in candidates[f"{count}"]:
            array.append(x * 5)
        if (x * 3) not in candidates[f"{count}"]:
            array.append(x * 3)
        if (x * 2) not in candidates[f"{count}"]:
            array.append(x * 2)
        if (x + 1) not in candidates[f"{count}"]:
            array.append(x + 1)
    else:
        for x in candidates[f"{count - 1}"]:
            if (x * 5) not in candidates[f"{count - 1}"] + array:
                array.append(x * 5)
            if (x * 3) not in candidates[f"{count - 1}"] + array:
                array.append(x * 3)
            if (x * 2) not in candidates[f"{count - 1}"] + array:
                array.append(x * 2)
            if (x + 1) not in candidates[f"{count - 1}"] + array:
                array.append(x + 1)

    return array


start = 1
candidates = {}
count = 1
while True:
    array = []
    array = calculation(start, array, candidates, count)
    if x in array:
        print(count)
        break
    candidates[f"{count}"] = array
    count += 1
    print(candidates)
