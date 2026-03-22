# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 공백과 줄바꿈 기준으로 한 번에 모두 분리해서 리스트로 만듭니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # K: 테스트 케이스의 개수
    K = int(input_data[0])
    idx = 1
    
    for x in range(1, K + 1):
        n = int(input_data[idx])      # 조상의 수
        k = int(input_data[idx + 1])  # 유전자의 길이
        idx += 2
        
        # 본인의 유전자
        my_traits = input_data[idx]
        idx += 1
        
        # 조상들의 유전자 리스트 저장
        ancestors = []
        for _ in range(n):
            ancestors.append(input_data[idx])
            idx += 1
            
        # 돌연변이 개수 세기
        mutant_count = 0
        
        # 각 유전자 위치(0 ~ k-1)마다 검사
        for i in range(k):
            is_mutant = True
            
            # 모든 조상들의 i번째 문자와 내 i번째 문자를 비교
            for ancestor in ancestors:
                if my_traits[i] == ancestor[i]:
                    # 한 명이라도 같으면 유전된 것이므로 돌연변이가 아님
                    is_mutant = False
                    break
                    
            # 아무와도 같지 않았다면 돌연변이 수 증가
            if is_mutant:
                mutant_count += 1
                
        # 문제에서 요구한 형식에 맞춰 출력
        print(f"Data Set {x}:")
        print(f"{mutant_count}/{k}")
        print() # 각 데이터 셋 끝에 빈 줄 출력

if __name__ == '__main__':
    solve()