def solution(my_string):
    answer = []
    for st in list(my_string):
        if st not in answer:
            answer.append(st)
    return ''.join(answer)