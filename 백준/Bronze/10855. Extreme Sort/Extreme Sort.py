# Gemini 2.5 Pro
import sys

def solve():
    """
    배열이 Extreme Property를 만족하는지 (즉, 오름차순으로 정렬되어 있는지) 확인합니다.
    """

    # 전체 입력을 읽고 공백으로 분리하여 리스트로 만듭니다.
    # N과 배열 A를 한 번에 처리하기 위함입니다.
    try:
        data = sys.stdin.read().split()
        if not data:
            return
    except Exception as e:
        # 입력이 없거나 오류 발생 시 종료
        # print(f"Input error: {e}", file=sys.stderr)
        return

    # 첫 번째 요소는 N입니다.
    try:
        N = int(data[0])
    except:
        # N이 유효한 숫자가 아닐 경우
        return

    # 나머지 요소는 배열 A입니다.
    # data[1]부터 N개의 요소를 정수로 변환하여 리스트 A를 만듭니다.
    try:
        A = [int(x) for x in data[1:N+1]]
    except ValueError:
        # 배열 요소가 숫자가 아닐 경우
        return

    # 배열 요소가 1개 이하일 경우 (N=1) 항상 정렬된 것으로 간주합니다.
    if N <= 1:
        print("yes")
        return

    # 배열을 순회하며 인접한 두 요소 A[i]와 A[i+1]를 비교합니다.
    # Extreme Property를 만족하려면 A[i] <= A[i+1] 여야 합니다.
    for i in range(N - 1):
        # 만약 A[i]가 다음 요소 A[i+1]보다 크다면 (A[i+1] < A[i]),
        # 즉, A[i+1] - A[i] < 0 이므로 Extreme Property가 깨집니다.
        if A[i] > A[i+1]:
            print("no")
            return

    # 반복문이 끝까지 실행되었다는 것은 모든 A[i] <= A[i+1] 조건을 만족한다는 뜻입니다.
    # 따라서 배열은 정렬되어 있고, Extreme Property가 성립합니다.
    print("yes")

if __name__ == "__main__":
    solve()