# GPT 5
import sys
input = sys.stdin.readline

# 1️⃣ T9 문자 → 숫자 매핑
t9 = {
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9'
}

# 2️⃣ 입력 처리
N = int(input().strip())
dictionary = [input().strip() for _ in range(N)]
S = input().strip()

# 3️⃣ 각 단어를 숫자 문자열로 변환하고 비교
count = 0
for word in dictionary:
    converted = ''.join(t9[ch] for ch in word)
    if converted == S:
        count += 1

# 4️⃣ 결과 출력
print(count)