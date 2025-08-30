# GPT 5
import sys

def main():
    M = 21252
    # CRT 계수 (23, 28, 33에 대한 미리 계산된 값)
    c1, c2, c3 = 5544, 14421, 1288  # (M/23)*inv(M/23 mod 23), (M/28)*inv(M/28 mod 28), (M/33)*inv(M/33 mod 33)

    case_no = 1
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        p, e, i, d = map(int, line.split())
        if p == -1 and e == -1 and i == -1 and d == -1:
            break

        # x ≡ p (mod 23), x ≡ e (mod 28), x ≡ i (mod 33)의 해
        x = (c1 * p + c2 * e + c3 * i) % M
        # 주어진 날짜 d 다음 트리플 피크까지의 일수 (d는 미포함)
        y = (x - d) % M
        if y == 0:
            y = M

        print(f"Case {case_no}: the next triple peak occurs in {y} days.")
        case_no += 1

if __name__ == "__main__":
    main()