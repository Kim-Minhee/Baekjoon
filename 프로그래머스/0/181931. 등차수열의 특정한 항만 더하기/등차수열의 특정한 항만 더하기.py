def solution(a, d, included):
    answer = 0
    for idx, chk in enumerate(included):
        if chk:
            answer += a + d * idx
    return answer