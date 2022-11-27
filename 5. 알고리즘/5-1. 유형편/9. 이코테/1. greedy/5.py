n, m = map(int, input().split(" "))
balls = list(map(int, input().split(" ")))

balls.sort()
result = 0
count = 1
for i in range(len(balls) - 1):
    if balls[i] == balls[i + 1]:
        count += 1
        continue
    result += count * (len(balls) - (i + 1))
    count = 1

print(result)
