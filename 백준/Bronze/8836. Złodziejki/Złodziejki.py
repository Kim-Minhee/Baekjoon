for _ in range(int(input())):
    N, K = map(int, input().split())

    a, b = N//(K-1), N%(K-1)
    if K==2 or b==1:
        print(0)
    elif b==0:
        print(1)
    else:
        print(K-b)