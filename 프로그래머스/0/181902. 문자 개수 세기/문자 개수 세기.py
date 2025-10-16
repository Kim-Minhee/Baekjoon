alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def solution(my_string):
    answer = []
    for a in alp:
        answer.append(my_string.count(a))
    return answer