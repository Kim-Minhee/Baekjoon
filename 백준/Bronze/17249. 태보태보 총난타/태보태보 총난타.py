S = input()

s1 = S.split('(')[0]
s2 = S.split(')')[1]

print(s1.count('@'), s2.count('@'))