s = input()

result = int(s[0])
for index in range(1, len(s)):
    result = max(result + int(s[index]), result * int(s[index]))
print(result)
