def solution(arr, delete_list):
    answer = [a for a in arr if a not in delete_list]
    return answer