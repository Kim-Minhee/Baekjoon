# GPT 4o
n = int(input())

for i in range(n):
    row_start = i * n + 1
    row_end = (i + 1) * n + 1
    row = list(range(row_start, row_end))
    
    if i % 2 == 1:  # 짝수 번째 줄 (인덱스 기준, 실제로는 홀수 줄): 오른쪽 → 왼쪽
        row.reverse()
    
    print(' '.join(map(str, row)))