# GPT
for _ in range(int(input())):
    N = int(input())
    min_area = float('inf')

    for a in range(1, int(N**(1/3))+2):
        if N%a!=0:
            continue
        bc = N//a
        for b in range(1, int((bc)**0.5) + 2):
            if bc%b!=0:
                continue
            c = bc//b
            surface_area = 2*(a*b + b*c + c*a)
            min_area = min(min_area, surface_area)

    print(min_area)