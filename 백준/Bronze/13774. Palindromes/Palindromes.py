import sys
input = sys.stdin.readline

for _ in range(30):
    W = input().strip()
    if W == '#':
        break

    is_possible = False
    for i in range(len(W)):
        temp = W[:i] + W[i + 1:]
        if temp == temp[::-1]:
            print(temp)
            is_possible = True
            break
    if not is_possible:
        print('not possible')