# Gemini 3 Pro
import sys

def solve():
    # 전체 입력을 한 번에 읽어와 공백/개행 기준으로 분리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 3줄의 문자열을 하나의 9글자 문자열로 이어 붙임
    face = "".join(input_data)
    
    # 1~6까지 가능한 모든 주사위 패턴 딕셔너리
    valid_faces = {
        "::::o::::": 1,
        "o:::::::o": 2,
        "::o:::o::": 2,
        "o:::o:::o": 3,
        "::o:o:o::": 3,
        "o:o:::o:o": 4,
        "o:o:o:o:o": 5,
        "o:oo:oo:o": 6,
        "ooo:::ooo": 6
    }
    
    # 패턴이 딕셔너리에 존재하면 값 출력, 아니면 unknown 출력
    if face in valid_faces:
        print(valid_faces[face])
    else:
        print("unknown")

if __name__ == '__main__':
    solve()