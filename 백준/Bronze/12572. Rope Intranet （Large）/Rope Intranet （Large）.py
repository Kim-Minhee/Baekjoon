# GPT 5.1
import sys
input = sys.stdin.readline

# Merge Sort 기반 inversion count 함수
def count_inversions(arr):
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr) // 2
    left_inv, left = count_inversions(arr[:mid])
    right_inv, right = count_inversions(arr[mid:])

    i = j = 0
    merged = []
    inv = left_inv + right_inv

    # merge 과정에서 inversion 계산
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i  # left쪽 남은 모든 원소가 inversion 발생

    merged.extend(left[i:])
    merged.extend(right[j:])

    return inv, merged

T = int(input().strip())
for t in range(1, T + 1):
    N = int(input().strip())
    wires = []

    for _ in range(N):
        A, B = map(int, input().split())
        wires.append((A, B))

    # A 기준으로 정렬
    wires.sort()

    # B 값만 뽑기 → 여기서 inversion count 수행
    B_list = [b for _, b in wires]

    inv_count, _ = count_inversions(B_list)

    print(f"Case #{t}: {inv_count}")