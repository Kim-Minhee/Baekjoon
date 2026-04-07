# Gemini 3.1 Pro
import sys

def solve():
    # 전체 입력을 한 번에 읽어와 공백 및 줄바꿈 기준으로 모두 분리합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 첫 4개의 값은 카테고리별 반영 비율입니다.
    percentages = {
        'Lab': int(input_data[0]),
        'Hw': int(input_data[1]),
        'Proj': int(input_data[2]),
        'Exam': int(input_data[3])
    }
    
    n = int(input_data[4])
    
    # 획득 점수(r)와 총점(s)을 누적할 딕셔너리를 초기화합니다.
    achieved = {'Lab': 0, 'Hw': 0, 'Proj': 0, 'Exam': 0}
    total = {'Lab': 0, 'Hw': 0, 'Proj': 0, 'Exam': 0}
    
    idx = 5
    for _ in range(n):
        cat = input_data[idx]            # 예: "Lab"
        # input_data[idx + 1] 은 "1:" 같은 식별자이므로 계산에 필요 없습니다.
        score_str = input_data[idx + 2]  # 예: "15/20"
        
        # "15/20" 형태의 문자열을 '/' 기준으로 분리하여 정수로 변환합니다.
        r, s = map(int, score_str.split('/'))
        
        # 해당 카테고리에 점수를 누적합니다.
        achieved[cat] += r
        total[cat] += s
        
        # 다음 입력(과제)을 처리하기 위해 인덱스를 3칸 이동합니다.
        idx += 3
        
    # 최종 점수 계산
    final_score = 0.0
    for cat in ['Lab', 'Hw', 'Proj', 'Exam']:
        # 카테고리별로 (총 획득 점수 / 총 만점) * 반영 비율을 계산하여 더합니다.
        final_score += percentages[cat] * (achieved[cat] / total[cat])
        
    # int()를 사용해 소수점 이하를 버림(truncate) 처리하고 출력합니다.
    print(int(final_score))

if __name__ == '__main__':
    solve()