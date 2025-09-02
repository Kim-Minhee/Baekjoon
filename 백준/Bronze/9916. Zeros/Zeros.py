# GPT 5
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    # n!을 직접 구해 문자열로 변환 후 '0'의 개수 세기
    fact_str = str(math.factorial(n))
    print(fact_str.count('0'))

if __name__ == "__main__":
    main()