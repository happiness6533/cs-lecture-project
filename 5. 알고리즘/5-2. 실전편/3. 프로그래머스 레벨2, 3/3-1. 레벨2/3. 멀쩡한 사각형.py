# 시간초과 해결이 안됨
import decimal


def solution(w, h):
    if w == h:
        return w * h - w
    elif w < h:
        half_count = 0
        for x in range(1, w + 1):
            result = decimal.Decimal(x * h) / decimal.Decimal(f"{w}")
            y = int(result)
            half_count += y
            if result == decimal.Decimal(f"{y}"):
                min_dump_count = x * y - ((half_count - y) * 2)
                multiply = w / x
                return int(w * h - (min_dump_count * multiply))
    else:
        half_count = 0
        for y in range(1, h + 1):
            result = decimal.Decimal(y * w) / decimal.Decimal(f"{h}")
            x = int(result)
            half_count += x
            if result == decimal.Decimal(f"{x}"):
                min_dump_count = x * y - ((half_count - x) * 2)
                multiply = w / x
                return int(w * h - (min_dump_count * multiply))


print(solution(8, 12))
