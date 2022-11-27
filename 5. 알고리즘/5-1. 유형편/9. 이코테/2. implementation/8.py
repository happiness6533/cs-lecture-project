string = list(input())
string.sort()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0
for i in range(len(string)):
    if string[i] in numbers:
        sum += int(string[i])
    else:
        for j in range(i, len(string)):
            print(string[j], end="")
        print(sum)
        break
