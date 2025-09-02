while True:
    A, B = input().split()
    if A == B == '#':
        break
    
    a, b = 0, 0
    for _ in range(int(input())):
        C, D = input().split()
        if C == D:
            a += 1
        else:
            b += 1
    
    print(A, a, B, b)