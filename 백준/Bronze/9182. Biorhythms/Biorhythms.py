case_num = 0
while True:
    P, E, I, D = map(int, input().split())
    if P == E == I == D == -1:
        break
    case_num += 1
    
    if P == E == I == 0:
        print(f'Case {case_num}: the next triple peak occurs in {21252 - D} days.')
    else:
        physical = [p for p in range(P % 23, 21253, 23)]
        emotional = [e for e in range(E % 28, 21253, 28)]
        intellectual = [i for i in range(I % 33, 21253, 33)]
    
        for day in physical:
            if day in emotional and day in intellectual:
                print(f'Case {case_num}: the next triple peak occurs in {day - D} days.')
                break