# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 받아 공백 단위로 분리합니다. (총 3개의 단어)
    words = sys.stdin.read().split()
    if not words:
        return
    
    # "bubble"과 "tapioka"가 아닌 단어만 걸러서 새로운 리스트에 담습니다.
    true_colors = [word for word in words if word not in ("bubble", "tapioka")]
    
    # 남은 단어가 없다면 "nothing"을 출력하고, 있다면 공백으로 이어붙여 출력합니다.
    if not true_colors:
        print("nothing")
    else:
        print(" ".join(true_colors))

if __name__ == "__main__":
    solve()