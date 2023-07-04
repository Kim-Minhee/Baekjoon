import math

w, h = map(int, input().split())
a = w*h/4840
print(math.ceil(a/5))