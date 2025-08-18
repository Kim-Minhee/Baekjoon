# Gemini 2.5 Pro
import sys

def solve_exam_grader():
    """
    정답지와 학생 답안을 비교하여 틀린 문제의 수를 계산합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스를 처리합니다.
    for case_num in range(1, num_test_cases + 1):
        try:
            # 문제의 수를 읽어옵니다. (실제 계산에는 길이를 직접 사용)
            num_questions = int(sys.stdin.readline())
            # 정답지와 학생 답안을 읽어옵니다.
            answer_key = sys.stdin.readline().strip()
            student_responses = sys.stdin.readline().strip()
        except (ValueError, IndexError):
            continue

        incorrect_count = 0
        # 각 문제를 순회하며 답을 비교합니다.
        for i in range(num_questions):
            if answer_key[i] != student_responses[i]:
                incorrect_count += 1
        
        # 최종 결과를 형식에 맞춰 출력합니다.
        print(f"Case {case_num}: {incorrect_count}")

# 함수 실행
solve_exam_grader()