# GPT
while True:
    X = input()
    if X == 'END':
        break

    i = 1
    prev = X
    while True:
        now = str(len(prev))
        if now==prev:
            print(i)
            break
        prev = now
        i += 1