def solution(brown, yellow):
    half_brown = brown // 2
    width_plus_height = half_brown + 2
    max_height = width_plus_height // 2
    for height in range(1, max_height + 1):
        width = width_plus_height - height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]