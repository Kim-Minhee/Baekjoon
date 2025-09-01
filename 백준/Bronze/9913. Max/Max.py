# GPT 5
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:1+n]

    # 값 범위가 1..1000이므로 고정 크기 배열로 빠르게 카운트
    counts = [0] * 1001
    for x in nums:
        counts[x] += 1

    print(max(counts))

if __name__ == "__main__":
    main()