import heapq


def solution(food_times, k):
    food_times = list(map(lambda pack: [pack[1], pack[0] + 1], enumerate(food_times)))

    pq = []
    for food_time in food_times:
        heapq.heappush(pq, food_time)

    total_time = 0
    while True:
        if len(pq) == 0:
            return -1

        min_food_time = heapq.heappop(pq)
        spin_time = min_food_time[0] * (len(pq) + 1)
        if total_time + spin_time >= k + 1:
            heapq.heappush(pq, min_food_time)
            pq.sort(key=lambda v: v[1])

            return pq[(k + 1 - total_time - 1) % len(pq)][1]

        total_time += min_food_time[0] * (len(pq) + 1)
        delete_cnt = 0
        for i in range(len(pq)):
            pq[i][0] -= min_food_time[0]
            if pq[i][0] == 0:
                delete_cnt += 1

        if delete_cnt > 0:
            for _ in range(delete_cnt):
                heapq.heappop(pq)
        # print(pq)


# 1
# 5, 2, 7, 2 >> 8초 뒤 >> 3, 0, 5, 0 (3) > 0 1 2 3 = 1
solution([3, 1, 2], 5)
