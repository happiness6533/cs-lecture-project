if __name__ == "__main__":
    n, k = map(int, input().split())

    result = 0
    while True:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        result += 1
        if n == 1:
            break

    print(result)
