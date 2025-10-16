def solution(q, r, code):
    answer = [c for i, c in enumerate(code) if i % q == r]
    return ''.join(answer)