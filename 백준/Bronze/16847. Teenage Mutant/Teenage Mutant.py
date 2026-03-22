# Gemini 3.1 Pro 피드백
import sys
input = sys.stdin.readline

# 전체 테스트 케이스 개수
for x in range(1, int(input().strip()) + 1):
    N, K = map(int, input().split())
    MY = input().strip()
    
    # [팁 1 적용] 조상들의 유전자를 딕셔너리가 아닌 리스트로 깔끔하게 모아둡니다.
    ancestors = [input().strip() for _ in range(N)]

    cnt = 0
    # [팁 2 적용] 내 유전자 1개와 조상들의 유전자 세로 묶음(튜플)을 동시에 꺼냅니다.
    for my_gene, ancestor_genes in zip(MY, zip(*ancestors)):
        # 내 유전자가 조상들의 세로 묶음 안에 없다면 돌연변이!
        if my_gene not in ancestor_genes:
            cnt += 1
            
    print(f'Data Set {x}:')
    print(f'{cnt}/{K}')
    print()