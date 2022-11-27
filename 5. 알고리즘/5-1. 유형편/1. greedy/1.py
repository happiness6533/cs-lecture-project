if __name__ == "__main__":
    m, n, k = map(int, input().split())
    input_list = list(map(int, input().split()))

    first_max = max(input_list)
    input_list.remove(first_max)
    second_max = max(input_list)
    input_list.remove(second_max)

    loop_count = int(n / (k + 1))
    rest_count = n % (k + 1)
    result = (first_max * k + second_max) * loop_count + first_max * rest_count

    print(result)
