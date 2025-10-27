def solution(sides):
    a, b = sorted(sides)
    answer1 = [i for i in range(b - a + 1, b + 1)]
    answer2 = [i for i in range(b + 1, a + b)]
    return len(set(answer1 + answer2))