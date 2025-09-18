while True:
    B = input()
    if B == '0':
        break
    current_num = B[0]
    current_cnt = 1
    r = []
    for i, b in enumerate(B[1:]):
        if b == current_num:
            current_cnt += 1
        else:
            r.append(current_cnt)
            r.append(current_num)
            current_num = b
            current_cnt = 1
        if i == len(B) - 2:
            r.append(current_cnt)
            r.append(current_num)
    print(''.join(map(str, r)))