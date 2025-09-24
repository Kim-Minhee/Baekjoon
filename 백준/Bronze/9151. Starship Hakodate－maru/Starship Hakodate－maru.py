# GPT 5
import sys
import bisect

MAXV = 151200

# 모든 비음수 정수의 세제곱수들 (<= MAXV)
cubes = []
n = 0
while True:
    v = n**3
    if v > MAXV:
        break
    cubes.append(v)
    n += 1

# 모든 비음수 정수의 사면체수들 T(n) = n(n+1)(n+2)/6 (<= MAXV)
tetras = []
n = 0
while True:
    v = n*(n+1)*(n+2)//6
    if v > MAXV:
        break
    tetras.append(v)
    n += 1

# 가능한 모든 합을 모아서 정렬 (중복 제거)
sums = set()
for c in cubes:
    for t in tetras:
        s = c + t
        if s <= MAXV:
            sums.add(s)
sums = sorted(sums)  # 오름차순 정렬

# 입력 처리
data = sys.stdin.read().strip().split()
out_lines = []
for tok in data:
    m = int(tok)
    if m == 0:
        break
    # sums에서 m 이하의 최대값을 찾음
    idx = bisect.bisect_right(sums, m)  # sums[0:idx] <= m
    if idx == 0:
        out_lines.append("0")
    else:
        out_lines.append(str(sums[idx-1]))

sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))