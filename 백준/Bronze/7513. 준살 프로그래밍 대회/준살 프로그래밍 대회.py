for t in range(1, int(input()) + 1):
    words = [input() for _ in range(int(input()))]
    
    passwords = []
    for _ in range(int(input())):
        PW = list(map(int, input().split()))
        pw = ''
        for i in PW[1:]:
            pw += words[i]
        passwords.append(pw)

    if t != 1:
        print()
    print(f'Scenario #{t}:')
    for pw in passwords:
        print(pw)