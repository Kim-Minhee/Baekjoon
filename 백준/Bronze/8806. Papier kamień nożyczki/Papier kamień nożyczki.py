for _ in range(int(input())):
    X1, Y1, Z1 = map(float, input().split())
    X2, Y2, Z2 = map(float, input().split())

    adam_win = X1 * Y2 + Y1 * Z2 + Z1 * X2
    gosia_win = X2 * Y1 + Y2 * Z1 + Z2 * X1
    if adam_win>gosia_win:
        print('ADAM')
    elif gosia_win>adam_win:
        print('GOSIA')
    else:
        print('=')