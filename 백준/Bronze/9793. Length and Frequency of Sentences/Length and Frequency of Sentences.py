import sys
input = sys.stdin.readline

sentences = {}
for _ in range(int(input().strip())):
    S = input().split()
    l = len(S)
    if l not in sentences.keys():
        sentences[l] = 1
    else:
        sentences[l] += 1

lengths = list(sentences.keys())
lengths.sort()
for length in lengths:
    print(length, sentences[length])