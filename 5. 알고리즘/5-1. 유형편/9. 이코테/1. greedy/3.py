# 11001100110011000001
s = input()

zeros_cnt = 0
ones_cnt = 0


if len(s) == 1:
    print(0)
else:
    i = 0
    while True:
        if s[i] == s[i + 1]:
            i += 1
            if i == len(s) - 1:
                if s[i] == "0":
                    zeros_cnt += 1
                else:
                    ones_cnt += 1
                break
            continue
        else:
            if s[i] == "0":
                zeros_cnt += 1
            else:
                ones_cnt += 1
            i += 1
            if i == len(s) - 1:
                if s[i] == "0":
                    zeros_cnt += 1
                else:
                    ones_cnt += 1
                break
    print(min(zeros_cnt, ones_cnt))