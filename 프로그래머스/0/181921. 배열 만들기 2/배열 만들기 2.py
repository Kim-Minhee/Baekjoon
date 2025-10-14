def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        num_str = set(str(num))
        if num_str == {'0', '5'} or num_str == {'0'} or num_str == {'5'}:
            answer.append(num)
    return [-1] if len(answer) == 0 else answer