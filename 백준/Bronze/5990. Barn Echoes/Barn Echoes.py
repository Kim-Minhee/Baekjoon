import sys
input = sys.stdin.readline

def count_overlap(suf, pre):
    for i in range(len(suf)):
        if pre.startswith(suf[i:]):
            return len(suf) - i
    return 0

M1, M2 = input().strip(), input().strip()
print(max(count_overlap(M1, M2), count_overlap(M2, M1)))