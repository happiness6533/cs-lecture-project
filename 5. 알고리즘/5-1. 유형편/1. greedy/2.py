if __name__ == "__main__":
    n, m = map(int, input().split())
    max_result = 1
    for i in range(n):
        row = list(map(int, input().split()))
        new_max = min(row)
        if new_max > max_result:
            max_result = new_max

    print(max_result)
