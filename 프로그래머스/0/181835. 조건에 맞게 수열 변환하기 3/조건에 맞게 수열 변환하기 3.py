def solution(arr, k):
    if k % 2 == 0:
        return [k + a for a in arr]
    else:
        return [k * a for a in arr]