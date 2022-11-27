n = input()

front_num = n[0:int(len(n) / 2)]
back_num = n[int(len(n) / 2):len(n)]

front_sum = sum(list(map(int, list(front_num))))
back_sum = sum(list(map(int, list(back_num))))

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")
