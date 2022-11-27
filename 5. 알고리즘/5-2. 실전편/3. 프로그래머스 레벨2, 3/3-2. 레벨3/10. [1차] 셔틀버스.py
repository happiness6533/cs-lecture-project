def convert_str_to_time(s_time):
    hour, mininute = s_time.split(":")
    hour = int(hour[1]) if hour[0] == 0 else int(hour)
    mininute = int(mininute[1]) if mininute[0] == 0 else int(mininute)

    return hour * 60 + mininute


def convert_time_to_str(time):
    hour = time // 60
    mininute = time % 60
    hour = f"0{hour}" if hour < 10 else f"{hour}"
    mininute = f"0{mininute}" if mininute < 10 else f"{mininute}"

    return hour + ":" + mininute


def solution(n, t, m, timetable):
    # TypeError: object of type 'NoneType' has no len() >> 자꾸 sort 결과를 리스트에 재대입하는 실수
    timetable = list(map(convert_str_to_time, timetable))
    timetable.sort()

    arrive_time = 9 * 60
    print(timetable)
    for i in range(n):
        for j in range(m):
            if len(timetable) == 0:
                if i == n - 1 and j == m - 2:
                    return convert_time_to_str(arrive_time)
                break
            if timetable[0] > arrive_time:
                if i == n - 1 and j == m - 2:
                    return convert_time_to_str(arrive_time)
                break
            if timetable[0] == arrive_time:
                if i == n - 1 and j == m - 2:
                    if len(timetable) == 1:
                        return convert_time_to_str(arrive_time)
                    else:
                        if timetable[1] == arrive_time:
                            return convert_time_to_str(arrive_time - 1)
                        else:
                            return convert_time_to_str(arrive_time)
                break
            if i == n - 1 and j == m - 2:
                if len(timetable) == 1:
                    return convert_time_to_str(arrive_time)
                else:
                    if timetable[1] == timetable[0]:
                        return convert_time_to_str(timetable[0] - 1)
                    else:
                        if timetable[1] <= arrive_time:
                            return convert_time_to_str(timetable[1] - 1)
                        else:
                            return convert_time_to_str(arrive_time)
                break
            del timetable[0]
            print(timetable)
        arrive_time += t


solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
