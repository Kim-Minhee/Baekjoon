def solution(code):
    mode = 0
    answer = ''
    for idx, ch in enumerate(code):
        if mode == 0:
            if ch == '1':
                mode = 1
            elif idx % 2 == 0:
                answer += ch
        else:
            if ch == '1':
                mode = 0
            elif idx % 2 != 0:
                answer += ch            
    return answer if answer != '' else 'EMPTY'