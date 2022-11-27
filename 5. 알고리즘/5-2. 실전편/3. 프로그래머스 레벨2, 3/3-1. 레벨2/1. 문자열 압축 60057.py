def solution(s):
    min_len = 1000
    for cut_len in range(1, len(s) + 1):
        str_list = []
        i = 0
        while True:
            str_list.append(s[i:i + cut_len])
            i += cut_len
            if i + cut_len > len(s) - 1:
                if s[i:len(s)] != "":
                    str_list.append(s[i:len(s)])
                break

        compressed_str_list = []
        start = str_list[0]
        cnt = 1
        if len(str_list) == 1:
            compressed_str_list.append(start)
        else:
            for i in range(1, len(str_list)):
                if str_list[i] != start:
                    compressed_str_list.append(f"{cnt}{start}" if cnt > 1 else start)
                    if i == len(str_list) - 1:
                        compressed_str_list.append(f"{str_list[i]}")
                    start = str_list[i]
                    cnt = 1  # 초기화를 할 때에는 모든 값을 초기화했는지 반드시 고려한다
                else:
                    cnt += 1
                    if i == len(str_list) - 1:
                        compressed_str_list.append(f"{cnt}{start}")

        compressed_str = "".join(compressed_str_list)
        if min_len > len(compressed_str):
            min_len = len(compressed_str)

    return min_len


solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
