N = int(input())
P = int(input())

q, r = divmod(P, N - 1)
min_p = P + q - 1
max_p = P + q
if r != 0:
    min_p += 1
    
print(min_p, max_p)