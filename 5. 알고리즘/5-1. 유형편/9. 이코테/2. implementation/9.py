def solution(s):
    answer = 0
    min_s = s
    for cut_len in range(1, len(s) // 2 + 1):
        result = ""
        i = 0
        while i <= len(s) - (len(s) % cut_len) - cut_len:
            count = 1
            sub_str = s[i: i + count * cut_len]
            while True:
                if i + (count + 1) * cut_len - 1 > len(s) - 1:
                    if count == 1:
                        compression_str = sub_str
                    else:
                        compression_str = str(count) + sub_str
                    result += compression_str
                    break

                next_sub_str = s[i + count * cut_len: i + (count + 1) * cut_len]
                if sub_str != next_sub_str:
                    if count == 1:
                        compression_str = sub_str
                    else:
                        compression_str = str(count) + sub_str
                    result += compression_str
                    break

                count += 1
            i += count * cut_len

        # aab bac cc
        # 8 % 3 => 2
        rest = len(s) % cut_len
        if rest != 0:
            result += s[-rest:]
        # print(cut_len, result)

        if len(result) < len(min_s):
            min_s = result
    return len(min_s)


print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("xababcdcdababcdcd"))  # 17

# s = "asdf g"
# a s d f g => 5 1/1/1/1/1 => 5 => 4
# as df g => 5 2/2/1 => 4 => 2
# asd fg => 5 3/2 => 3 => 0
