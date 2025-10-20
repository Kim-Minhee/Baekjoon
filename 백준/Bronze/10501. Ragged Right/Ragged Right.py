sentences = []
max_len = 0
while True:
    try:
        S = input().strip()
        sentences.append(S)
        if len(S) > max_len:
            max_len = len(S)
    except:
        break

p = 0
for s in sentences[:-1]:
    p += (max_len - len(s)) ** 2
print(p)