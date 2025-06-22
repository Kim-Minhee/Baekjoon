# GPT 4o
keyword = input().strip()
message = input().strip()

# 1. 알파벳 문자만 추출
filtered = ''.join([ch for ch in message if ch.isalpha()])

# 2. 열 개수 = 키워드 길이
cols = len(keyword)

# 3. 각 열별 shift 값 계산
shifts = [ord(ch) - ord('A') for ch in keyword]

# 4. 메시지를 블록으로 나눔 (열 단위로 접근하기 쉽게 행 단위 저장)
rows = []
for i in range(0, len(filtered), cols):
    rows.append(list(filtered[i:i+cols]))

# 5. 시프트 적용
for r in range(len(rows)):
    for c in range(len(rows[r])):
        original = rows[r][c]
        shift = shifts[c]
        shifted = chr((ord(original) - ord('A') + shift) % 26 + ord('A'))
        rows[r][c] = shifted

# 6. 최종 결과: 행 우선 순서로 출력
encoded = ''.join(''.join(row) for row in rows)
print(encoded)