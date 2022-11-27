def solution(bridge_length, weight, truck_weights):
    stack = []
    time = 0
    while len(truck_weights) != 0 or len(stack) != 0:
        if len(stack) >= 1:
            for truck_in_stack in stack:
                truck_in_stack[1] = truck_in_stack[1] + 1
            if stack[-1][1] == bridge_length:
                stack.pop()
        if len(truck_weights) == 0:
            time += 1
            continue
        current_total_weight = sum(list(map(lambda x: x[0], stack)))
        if len(stack) < bridge_length and current_total_weight + truck_weights[0] <= weight:
            truck = [truck_weights[0], 0]
            truck_weights = truck_weights[1:]
            stack.insert(0, truck)
        time += 1

    return time