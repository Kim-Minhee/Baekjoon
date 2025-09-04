# GPT 5
import sys

def main():
    tokens = sys.stdin.read().split()
    it = iter(tokens)

    t = int(next(it))
    out = []

    for case_no in range(1, t + 1):
        out.append(f"Scenario #{case_no}:")

        m = int(next(it))
        words = [next(it) for _ in range(m)]  # 0-based 인덱스

        n = int(next(it))
        for _ in range(n):
            k = int(next(it))
            idxs = [int(next(it)) for _ in range(k)]  # 0-based 인덱스가 그대로 들어옴
            password = "".join(words[j] for j in idxs)
            out.append(password)

        if case_no != t:
            out.append("")  # 테스트 케이스 사이 빈 줄

    print("\n".join(out))

if __name__ == "__main__":
    main()