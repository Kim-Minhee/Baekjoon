# GPT 5
import sys

def max_height(n: int) -> int:
    h = 0
    used = 0
    # 다음 층(h+1)을 올리기 위해 필요한 블록 수: 2h^2 + 2h + 1
    while True:
        need = 2*h*h + 2*h + 1
        if used + need > n:
            return h
        used += need
        h += 1

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    print(max_height(n))

if __name__ == "__main__":
    main()