# GPT 5
import sys

def main():
    input = sys.stdin.readline
    out_lines = []

    while True:
        line = input()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        if line == "# #":
            break

        # 첫 줄: 플레이어 두 명의 이름
        a, b = line.split()

        # 둘째 줄: 기록된 던지기 횟수 n
        n_line = input()
        while n_line is not None and n_line.strip() == "":
            n_line = input()
        if not n_line:
            break
        n = int(n_line.strip())

        # n개의 기록 처리
        sa = sb = 0
        for _ in range(n):
            toss = input().strip()
            while toss == "":
                toss = input().strip()
            call, result = toss.split()
            if call == result:
                sa += 1
            else:
                sb += 1

        out_lines.append(f"{a} {sa} {b} {sb}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()