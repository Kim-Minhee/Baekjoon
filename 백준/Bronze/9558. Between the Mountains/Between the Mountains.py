# GPT 5
import sys

def min_diff_between_mountains(a, b):
    a.sort()
    b.sort()
    i = j = 0
    best = 10**9  # 충분히 큰 값

    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < best:
            best = diff
            if best == 0:  # 더 이상 줄어들 수 없음
                break
        # 두 포인터 이동
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out_lines = []

    for _ in range(t):
        n1 = data[idx]; idx += 1
        a = data[idx:idx+n1]; idx += n1

        n2 = data[idx]; idx += 1
        b = data[idx:idx+n2]; idx += n2

        out_lines.append(str(min_diff_between_mountains(a, b)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()