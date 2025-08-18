# GPT 5
T = int(input())  # 테스트 케이스 개수

for case in range(1, T + 1):
    L = int(input())        # 문제 수
    answer_key = input().strip()   # 정답 키
    student = input().strip()      # 학생 답안
    
    # 정답과 다른 경우를 세기
    incorrect = sum(1 for a, b in zip(answer_key, student) if a != b)
    
    print(f"Case {case}: {incorrect}")