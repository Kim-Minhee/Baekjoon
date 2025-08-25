def string_id(word):
    return word[1:]

while True:
    N = int(input())
    if N == 0:
        break

    words = set()
    for _ in range(N):
        W = input()
        words.add(W)

    cnt = 0
    while True:
        deleted = []
        for word in words:
            if len(word) != 1:
                deleted.append(string_id(word))
        words = set(deleted)
        if len(words) != N:
            break
        cnt += 1

    print(cnt)