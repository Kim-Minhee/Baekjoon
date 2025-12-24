# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.read().split() 사용
def solve():
    """
    루프 음악의 피크 개수를 계산하는 함수
    양쪽 이웃보다 크거나(최대), 양쪽 이웃보다 작으면(최소) 피크로 간주합니다.
    """
    # Ler toda a entrada de uma vez para eficiência
    # 모든 입력을 공백 단위로 분리하여 한 번에 읽습니다.
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        while True:
            # N: Número de amostras (샘플 수)
            N = int(next(iterator))
            
            # Condição de parada (종료 조건): N = 0
            if N == 0:
                break
            
            H = []
            for _ in range(N):
                H.append(int(next(iterator)))
            
            peaks = 0
            
            # Verificar cada amostra no loop (모든 샘플 순회)
            for i in range(N):
                # Valor atual (현재 값)
                curr_val = H[i]
                
                # Valor anterior (이전 값)
                # Python에서 인덱스 -1은 리스트의 마지막 요소를 가리키므로
                # i=0일 때 H[-1] (즉, H[N-1])을 참조하여 루프 구조가 자연스럽게 처리됩니다.
                prev_val = H[i-1]
                
                # Próximo valor (다음 값)
                # 모듈러 연산(%)을 사용하여 i가 마지막(N-1)일 때 0번 인덱스를 참조하도록 합니다.
                next_val = H[(i+1) % N]
                
                # Pico máximo local (지역 최대값 확인)
                if prev_val < curr_val and curr_val > next_val:
                    peaks += 1
                # Pico mínimo local (지역 최소값 확인)
                elif prev_val > curr_val and curr_val < next_val:
                    peaks += 1
                    
            print(peaks)
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()