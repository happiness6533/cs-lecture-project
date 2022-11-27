def solution(record):
    answer = []

    users = {}
    records = {}
    for line in record:
        line = line.strip().split(" ")
        if line[0] == "Enter":
            if line[1] not in users.keys():
                users[line[1]] = line[2]
            else:
                if users[line[1]] != line[2]:
                    temp = len(users[line[1]])

                    users[line[1]] = line[2]

                    users[line[1]] = line[2]
                    for record_index in records[line[1]]:
                        answer[record_index] = line[2] + answer[record_index][temp:]

            if line[1] not in records.keys():
                records[line[1]] = [len(answer)]
            else:
                records[line[1]].append(len(answer))
            answer.append(f"{line[2]}님이 들어왔습니다.")
        elif line[0] == "Leave":
            records[line[1]].append(len(answer))
            answer.append(f"{users[line[1]]}님이 나갔습니다.")
        else:
            temp = len(users[line[1]])
            users[line[1]] = line[2]
            for record_index in records[line[1]]:
                answer[record_index] = line[2] + answer[record_index][temp:]

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
