def solution(n, results):
    answer = 0

    fixed_players = []
    for player in range(1, n + 1):
        strongers = []
        weakers = []
        for result in results:
            [stronger, weaker] = result
            if weaker == player:
                strongers.append(stronger)
            elif stronger == player:
                weakers.append(weaker)
            elif weaker in strongers:
                strongers.append(stronger)
            elif stronger in weakers:
                weakers.append(weaker)
        for result in results:
            [stronger, weaker] = result
            if weaker == player:
                strongers.append(stronger)
            elif stronger == player:
                weakers.append(weaker)
            elif weaker in strongers:
                strongers.append(stronger)
            elif stronger in weakers:
                weakers.append(weaker)
        for result in results:
            [stronger, weaker] = result
            if weaker == player:
                strongers.append(stronger)
            elif stronger == player:
                weakers.append(weaker)
            elif weaker in strongers:
                strongers.append(stronger)
            elif stronger in weakers:
                weakers.append(weaker)
        for result in results:
            [stronger, weaker] = result
            if weaker == player:
                strongers.append(stronger)
            elif stronger == player:
                weakers.append(weaker)
            elif weaker in strongers:
                strongers.append(stronger)
            elif stronger in weakers:
                weakers.append(weaker)
        if len(list(set(strongers + weakers))) == n - 1:
            fixed_players.append([player, len(list(set(strongers))) + 1])
            answer += 1
    for fixed_player in fixed_players:
        [player, ranking] = fixed_player
        if ranking == n - 1:
            for result in results:
                [stronger, weaker] = result
                if stronger == player:
                    if [weaker, n] not in fixed_players:
                        fixed_players.append([weaker, n])
        elif ranking == 2:
            for result in results:
                [stronger, weaker] = result
                if weaker == player:
                    if [stronger, 1] not in fixed_players:
                        fixed_players.append([stronger, 1])


    return len(fixed_players)


solution(5, [[4, 3],
             [4, 2],
             [3, 2],
             [1, 2],
             [2, 5]])
