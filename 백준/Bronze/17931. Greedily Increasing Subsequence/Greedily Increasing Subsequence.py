# Gemini 3.1 Pro
import sys

def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = input_data[1:]
    
    gis = []
    # 첫 번째 원소는 무조건 포함 (g1 = a1)
    current_max = int(a[0])
    gis.append(str(current_max))
    
    # 두 번째 원소부터 순회하며 현재 최댓값보다 큰 경우만 추가
    for i in range(1, n):
        num = int(a[i])
        if num > current_max:
            current_max = num
            gis.append(str(num))
    
    # 출력 형식에 맞춰 길이와 수열 출력
    print(len(gis))
    print(" ".join(gis))

if __name__ == "__main__":
    solve()