for _ in range(int(input())):
    A, B = map(set, input().split())
    if A==B:
        print('YES')
    else:
        print('NO')