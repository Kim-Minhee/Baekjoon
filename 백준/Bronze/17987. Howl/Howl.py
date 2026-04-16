# Gemini 3.1 Pro
import sys

def solve():
    # 펜리르의 울음소리를 읽어옵니다. (최대 1MB이므로 sys.stdin.readline 사용)
    fenrir_howl = sys.stdin.readline().strip()

    if not fenrir_howl:
        return

    # 펜리르보다 긴 울음소리의 길이를 정합니다.
    target_length = len(fenrir_howl) + 1

    # 기본 필수 문자열 "AWH" (H 뒤에 W/A가 오면 안 되므로 W를 앞에 둠)
    # 그 뒤를 모두 "O"로 채우면 모든 조건을 만족합니다.
    # 최소 길이는 A, H, O, W가 다 들어가야 하므로 4 이상이어야 합니다.
    # 하지만 펜리르의 소리가 이미 유효하므로 len+1은 항상 4 이상입니다.

    result = "AWH" + "O" * (target_length - 3)

    print(result)

if __name__ == "__main__":
    solve()