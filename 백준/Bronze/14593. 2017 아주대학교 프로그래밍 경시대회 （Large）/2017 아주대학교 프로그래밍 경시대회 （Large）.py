import sys
input = sys.stdin.readline

participants = []
for i in range(1, int(input().strip()) + 1):
    S, C, L = map(int, input().split())
    participants.append((S, C, L, i))
sorted_participants = sorted(participants, key = lambda x : (-x[0], x[1], x[2]))
print(sorted_participants[0][-1])