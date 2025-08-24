# GPT 5
def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    t = int(input())
    for _ in range(t):
        i, dv = map(int, input().split())
        xi, yi = points[i - 1]  # 입력은 1-based라서 보정
        dv2 = dv * dv

        count = 0
        for j, (x, y) in enumerate(points):
            if j == i - 1:  # 자기 자신 제외
                continue
            if (xi - x) ** 2 + (yi - y) ** 2 <= dv2:
                count += 1
        print(count)

if __name__ == "__main__":
    main()