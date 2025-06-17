# GPT 4o
# 입력 처리
mother = input()
father = input()

dominant = 'ABCDE'
recessive = 'abcde'
possible_genes = []

# 각 유전자 자리마다 가능한 표현형을 계산
for i in range(0, 10, 2):
    m_alleles = [mother[i], mother[i+1]]
    f_alleles = [father[i], father[i+1]]
    gene_idx = i // 2
    expressions = set()

    # 부모의 각각의 알렐 조합 생성
    for m in m_alleles:
        for f in f_alleles:
            if m.isupper() or f.isupper():
                expressions.add(dominant[gene_idx])  # dominant 표현
            else:
                expressions.add(recessive[gene_idx])  # recessive 표현
    possible_genes.append(expressions)

# 아기 유전자 검사
for _ in range(int(input())):
    baby = input()
    for i in range(5):
        if baby[i] not in possible_genes[i]:
            print("Not their baby!")
            break
    else:
        print("Possible baby.")