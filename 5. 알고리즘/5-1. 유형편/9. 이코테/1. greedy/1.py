n = int(input())
all_x = list(map(int, input().split(" ")))

all_x.sort()
num_of_friends = 0
count_of_team = 0

for x in all_x:
    num_of_friends += 1
    if num_of_friends == x:
        count_of_team += 1
        num_of_friends = 0
print(count_of_team)
