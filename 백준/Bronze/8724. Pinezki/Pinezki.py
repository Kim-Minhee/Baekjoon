N = int(input())
A = list(map(int, input().split()))

A += [0]
max_pin, pin = 0, 0
for a in A:
    if a==1:
        pin += 1
    else:
        if pin>max_pin:
            max_pin = pin
        pin = 0

print(max_pin)