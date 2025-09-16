# GPT 5
def happiness(first_value, decrement, count):
    """count마리 동물이 주는 행복 계산"""
    total = 0
    for i in range(count):
        val = first_value - i * decrement
        if val <= 0:
            break
        total += val
    return total


def main():
    import sys
    input = sys.stdin.readline

    M, D_M = map(int, input().split())
    H, D_H = map(int, input().split())
    N = int(input())

    total_happiness = 0
    for _ in range(N):
        C, B = map(int, input().split())
        milk_happiness = happiness(M, D_M, C)
        honey_happiness = happiness(H, D_H, B)
        total_happiness += max(milk_happiness, honey_happiness)

    print(total_happiness)


if __name__ == "__main__":
    main()