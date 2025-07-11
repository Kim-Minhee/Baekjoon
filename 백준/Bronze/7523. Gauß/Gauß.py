# GPT 4o
T = int(input())

for i in range(1, T + 1):
    n, m = map(int, input().split())
    total = (m - n + 1) * (n + m) // 2

    print(f"Scenario #{i}:")
    print(total)
    print()