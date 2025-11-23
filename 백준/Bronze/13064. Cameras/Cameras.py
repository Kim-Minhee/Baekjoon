# GPT 5
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    s = input().strip()
    
    # 길이 검사
    if len(s) != 8:
        continue
    
    # 조건 검사
    ok = True
    
    # 1~2번째: 1~9, 같아야 함
    if not (s[0].isdigit() and s[1].isdigit() and '1' <= s[0] <= '9' and s[0] == s[1]):
        ok = False
    
    # 3~4번째: 1~9
    if not (s[2].isdigit() and s[3].isdigit() and '1' <= s[2] <= '9' and '1' <= s[3] <= '9'):
        ok = False
    
    # 5번째: 대문자 영어 알파벳
    if not ('A' <= s[4] <= 'Z'):
        ok = False
    
    # 6~8번째: 1~9
    for ch in s[5:8]:
        if not (ch.isdigit() and '1' <= ch <= '9'):
            ok = False
            break
    
    if ok:
        print(s)