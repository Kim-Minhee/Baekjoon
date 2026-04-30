from collections import Counter

def solution(participant, completion):
    part_count = Counter(participant)
    comp_count = Counter(completion)
    for comp, count in comp_count.items():
        part_count[comp] -= count
    return part_count.most_common(1)[0][0]