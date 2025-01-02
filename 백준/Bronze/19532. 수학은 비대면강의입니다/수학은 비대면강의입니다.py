# 연립방정식
a, b, c, d, e, f = map(int, input().split())

y = (a*f-d*c)//(a*e-b*d)
x = (e*c-b*f)//(a*e-b*d)
print(int(x), int(y))