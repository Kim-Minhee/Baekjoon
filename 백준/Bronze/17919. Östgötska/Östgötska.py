# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 공백 단위로 쪼개어 단어 리스트를 만듭니다.
    words = sys.stdin.read().split()
    
    if not words:
        return
        
    total_words = len(words)
    
    # 'ae'가 포함된 단어의 개수를 sum과 제너레이터로 아주 짧게 셉니다.
    ae_count = sum(1 for word in words if 'ae' in word)
    
    # 비율이 40% 이상인지 확인 (0.4 이상)
    if ae_count / total_words >= 0.4:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

if __name__ == '__main__':
    solve()