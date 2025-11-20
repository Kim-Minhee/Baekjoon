# GPT 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = str(N) * N   # N을 N번 반복한 문자열
print(result[:M])     # 앞에서 M자리만 출력