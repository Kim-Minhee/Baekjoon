# Gemini 2.5 Pro
import sys
# sys.stdin.readline을 input 함수로 정의하여 입력을 빠르게 처리합니다.
input = sys.stdin.readline 

def solve():
    """
    베이커의 백분율을 사용하여 레시피의 재료 무게를 조정하고 출력합니다.
    """
    try:
        # 테스트 케이스의 개수 T를 읽습니다.
        T_line = input().strip()
        if not T_line:
            return
            
        T = int(T_line)

        # T개의 테스트 케이스를 순회합니다.
        for case_num in range(1, T + 1):
            # R (재료 수), P (원래 분량), D (원하는 분량)을 읽습니다.
            try:
                R, P, D = map(int, input().split())
            except Exception:
                # 빈 줄이나 잘못된 입력이 들어오면 해당 케이스를 건너뜁니다.
                continue

            # 스케일링 인자(Scaling Factor) 계산: (원하는 분량 / 원래 분량)
            scaling_factor = D / P

            ingredients = []
            main_ingredient_scaled_weight = 0.0

            # 1. 모든 재료 데이터를 읽고, 메인 재료(100%)의 스케일링된 무게를 계산합니다.
            for _ in range(R):
                line = input().split()
                if not line:
                    continue
                    
                name = line[0]
                weight = float(line[1])
                percentage = float(line[2])
                
                # 순서 유지를 위해 재료 정보를 저장합니다.
                ingredients.append((name, weight, percentage))

                # 메인 재료(100.0%)를 찾아 스케일링된 무게를 계산합니다.
                if percentage == 100.0:
                    # 메인 재료의 스케일링된 무게 = 원래 무게 * 스케일링 인자
                    main_ingredient_scaled_weight = weight * scaling_factor
            
            # 2. 결과 출력 시작: 레시피 번호 (공백 수정)
            sys.stdout.write(f"Recipe # {case_num}\n")
            
            # 3. 모든 재료의 스케일링된 무게를 계산하고 출력합니다.
            #    (메인 재료 자신도 이 공식에 의해 정확히 계산됩니다.)
            for name, weight, percentage in ingredients:
                # 다른 모든 재료의 스케일링된 무게 계산: 
                # (재료 비율 / 100) * (스케일링된 메인 재료 무게)
                # 예: (11.2 / 100.0) * 2268.0 = 254.016
                # 메인 재료: (100.0 / 100.0) * 2268.0 = 2268.0
                scaled_weight = (percentage / 100.0) * main_ingredient_scaled_weight
                
                # 소수점 이하 첫째 자리까지 출력 (문제 요구사항)
                sys.stdout.write(f"{name} {scaled_weight:.1f}\n")
            
            # 케이스 종료 후 구분선 출력
            sys.stdout.write("-" * 40 + "\n")

    except Exception:
        # 예외 발생 시 처리를 위한 부분 (일반적인 코딩 테스트 환경에서는 생략 가능)
        pass

if __name__ == "__main__":
    solve()