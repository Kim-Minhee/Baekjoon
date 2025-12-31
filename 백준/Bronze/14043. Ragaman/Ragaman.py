# Gemini 3 Pro
import sys
from collections import Counter

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    와일드카드 아나그램 판별 함수
    두 번째 문자열의 알파벳 빈도수가 첫 번째 문자열의 빈도수를 초과하지 않는지 확인합니다.
    (와일드카드 '*'는 부족한 문자를 채우는 역할을 하므로 검사에서 제외)
    """
    try:
        # 두 문자열 입력 (공백 제거)
        s1 = input().strip()
        s2 = input().strip()
        
        # 각 문자열의 문자 빈도수 계산
        count1 = Counter(s1)
        count2 = Counter(s2)
        
        # s2에 있는 모든 문자를 순회하며 확인
        for char, count in count2.items():
            # 와일드카드는 검사 대상이 아님
            if char == '*':
                continue
            
            # s2가 가진 특정 문자의 개수가 s1보다 많으면 불가능
            # (s1에 없는 문자가 s2에 있거나, 개수가 더 많은 경우)
            if count > count1[char]:
                print('N')
                return
        
        # 모든 조건을 통과하면 가능
        print('A')

    except Exception:
        pass

if __name__ == "__main__":
    solve()