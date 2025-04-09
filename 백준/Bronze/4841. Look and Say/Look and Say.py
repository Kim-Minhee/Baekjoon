# GPT
from itertools import groupby

for _ in range(int(input())):
    S = input()
    result = ''
    for digit, group in groupby(S):
        count = len(list(group))
        result += str(count) + digit
    print(result)