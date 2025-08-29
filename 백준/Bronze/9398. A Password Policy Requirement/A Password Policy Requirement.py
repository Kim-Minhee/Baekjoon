# GPT 5
import sys

def shortest_valid_substring_len(s: str) -> int:
    n = len(s)
    if n < 6:
        return 0

    # 카테고리: 0=대문자, 1=소문자, 2=숫자
    def cat_idx(ch: str) -> int:
        if 'A' <= ch <= 'Z':
            return 0
        elif 'a' <= ch <= 'z':
            return 1
        elif '0' <= ch <= '9':
            return 2
        return -1  # 문제 조건상 오지 않음

    counts = [0, 0, 0]
    left = 0
    best = float('inf')

    for right, ch in enumerate(s):
        idx = cat_idx(ch)
        if idx >= 0:
            counts[idx] += 1

        # 윈도우가 조건(대/소/숫자 모두 포함 + 길이>=6)을 만족하면 최대한 줄이기
        while (right - left + 1) >= 6 and all(c > 0 for c in counts):
            best = min(best, right - left + 1)
            # 왼쪽을 한 칸 줄여서 더 짧은 해를 시도
            lidx = cat_idx(s[left])
            if lidx >= 0:
                counts[lidx] -= 1
            left += 1

    return 0 if best == float('inf') else best

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0].strip())
    out = []
    for i in range(1, t + 1):
        s = data[i].strip()
        out.append(str(shortest_valid_substring_len(s)))
    print("\n".join(out))

if __name__ == "__main__":
    main()