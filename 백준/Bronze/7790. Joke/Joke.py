# GPT 4o
import sys

# 전체 입력 텍스트 읽기 (파일 크기 최대 20KB)
text = sys.stdin.read()

# 'joke'라는 부분 문자열 개수 세기
count = text.count('joke')

# 결과 출력
print(count)