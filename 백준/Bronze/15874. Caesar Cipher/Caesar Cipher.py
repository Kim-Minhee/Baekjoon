# Gemini 3 Pro
import sys

def solve():
    # 빠른 입출력
    input = sys.stdin.readline
    
    # k: 밀 횟수, l: 문자열 길이 (l은 파이썬에서 굳이 사용하지 않아도 무방함)
    k_str, l_str = input().split()
    k = int(k_str)
    
    # 두 번째 줄의 문자열 입력 (공백, 온점 등 포함이므로 개행 문자만 제거)
    s = input().rstrip('\n')
    
    # 26번마다 제자리로 돌아오므로 26으로 나눈 나머지 연산
    k %= 26
    
    ans = []
    
    for char in s:
        # 대문자일 경우
        if 'A' <= char <= 'Z':
            # 0~25로 맞춘 뒤 k만큼 이동, 26으로 나눈 나머지를 구하고 다시 대문자 영역으로
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            ans.append(shifted)
            
        # 소문자일 경우
        elif 'a' <= char <= 'z':
            # 0~25로 맞춘 뒤 k만큼 이동, 26으로 나눈 나머지를 구하고 다시 소문자 영역으로
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            ans.append(shifted)
            
        # 공백, 쉼표, 온점 등은 그대로
        else:
            ans.append(char)
            
    # 리스트에 모은 문자들을 한 번에 문자열로 합쳐서 출력
    print("".join(ans))

if __name__ == '__main__':
    solve()