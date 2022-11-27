import decimal

def solution(lines):
    answer = 0

    logs = []
    times = []
    for line in lines:
        line = line.split(" ")
        [_, end_time, duration] = line
        [h, m, s] = end_time.split(":")
        end_time = decimal.Decimal(h) * 3600 + decimal.Decimal(m) * 60 + decimal.Decimal(s.split(".")[0]) + decimal.Decimal("0." + s.split(".")[1])
        duration = decimal.Decimal(duration[:-1])
        start_time = end_time - duration + decimal.Decimal("0.001")
        logs.append([start_time, end_time])
        times.append(start_time)
        times.append(end_time)

    max_count = 0
    for time in times:
        count = 0
        for log in logs:
            if log[1] < time or decimal.Decimal(f"{time}") + decimal.Decimal("1") - decimal.Decimal("0.001") < log[0]:
                continue
            count += 1
        if count > max_count:
            max_count = count
    answer = max_count

    return answer


solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
])
