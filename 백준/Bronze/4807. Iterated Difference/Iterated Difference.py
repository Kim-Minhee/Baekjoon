# GPT
case = 1
while True:
    N = int(input())
    if N == 0:
        break

    lst = list(map(int, input().split()))
    for iteration in range(1, 1001):
        if len(set(lst)) == 1:
            print(f'Case {case}: {iteration - 1} iterations')
            break
        lst = [abs(a - b) for a, b in zip(lst, lst[1:] + lst[:1])]
    else:
        print(f'Case {case}: not attained')

    case += 1