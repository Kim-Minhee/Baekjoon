# Gemini 3 Pro
import sys

def solve():
    # 입력 받기
    # 한 줄에 10개의 정수가 주어집니다.
    try:
        nums = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    # 0이 아닌 두 수의 인덱스와 값을 저장할 리스트
    known = []
    for i in range(10):
        if nums[i] != 0:
            known.append((i, nums[i]))
    
    # known 리스트에는 [(idx1, val1), (idx2, val2)] 형태가 저장됨
    idx1, val1 = known[0]
    idx2, val2 = known[1]
    
    # 인덱스 차이와 값의 차이 계산
    idx_diff = idx2 - idx1
    val_diff = val2 - val1
    
    # 정수 공차를 만들 수 있는지 확인 (나누어 떨어져야 함)
    if val_diff % idx_diff != 0:
        print("-1")
        return
    
    # 공차(d) 계산 (정수 나눗셈 // 사용)
    d = val_diff // idx_diff
    
    # 전체 수열 복원
    result = []
    for k in range(10):
        # 기준점(idx1, val1)을 이용하여 k번째 값을 계산
        # 공식: A_k = val1 + (k - idx1) * d
        term = val1 + (k - idx1) * d
        result.append(term)
        
    # 결과 출력 (공백으로 구분하여 한 줄에 출력)
    print(*(result))

if __name__ == "__main__":
    solve()