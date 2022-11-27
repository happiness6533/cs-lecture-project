import heapq

n = int(input())

q = []
heapq.heappush(q, 1)
for i in range(n):
    v = heapq.heappop(q)
    if v * 2 not in q:
        heapq.heappush(q, v * 2)
    if v * 3 not in q:
        heapq.heappush(q, v * 3)
    if v * 5 not in q:
        heapq.heappush(q, v * 5)
    if i == n - 1:
        print(v)
