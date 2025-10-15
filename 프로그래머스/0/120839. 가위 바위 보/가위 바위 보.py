rsp_win = {'2':'0', '0':'5', '5':'2'}

def solution(rsp):
    return ''.join(rsp_win[a] for a in rsp)