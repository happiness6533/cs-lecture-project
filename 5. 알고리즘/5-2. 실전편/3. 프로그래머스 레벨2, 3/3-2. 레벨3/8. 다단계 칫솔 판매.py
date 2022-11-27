def solution(enroll, referral, seller, amount):
    answer = []

    company_structure = {}
    money_structure = {}
    for i in range(len(enroll)):
        company_structure[enroll[i]] = referral[i]
        money_structure[enroll[i]] = 0
    for i in range(len(seller)):
        member = seller[i]
        money = amount[i] * 100
        while member in company_structure.keys():
            not_my_money = int(money * 0.1)
            if not_my_money < 1:
                money_structure[member] += money
                break
            money_structure[member] += money - not_my_money
            member = company_structure[member]
            money = not_my_money

    answer = list(money_structure.values())

    return answer