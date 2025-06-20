# GPT 4o
for _ in range(int(input())):
    words = [input() for _ in range(3)]
    fix_free = True
    for i in range(3):
        for j in range(3):
            if i != j and (words[i].startswith(words[j]) or words[i].endswith(words[j])):
                fix_free = False
    print('Yes' if fix_free else 'No')