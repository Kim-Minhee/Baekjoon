# Gemini 2.5 Pro
import sys

def solve_library_labels():
    """
    각 도서관의 책 라벨이 가로로 붙여질지 세로로 붙여질지 결정합니다.
    """
    # '#'가 입력될 때까지 여러 도서관 시나리오를 처리합니다.
    while True:
        try:
            # 첫 줄에서 도서관 이름과 폰트 너비를 읽어옵니다.
            line = sys.stdin.readline().split()
            if not line: break # 입력이 끝나면 종료

            library_name = line[0]
            # 두 번째 요소가 없을 경우를 대비하여 예외 처리
            if len(line) < 2: continue
            
            font_width_str = line[1]
        except IndexError:
            break

        # 전체 입력 종료 조건 확인
        if library_name == '#' and font_width_str == '0':
            break
        
        font_width = int(font_width_str)
        
        # --- 수정된 부분 1: 도서관 이름 출력 형식 변경 ---
        print(f"{library_name} Library")

        try:
            # 처리할 책의 수를 읽어옵니다.
            num_books = int(sys.stdin.readline())
        except (ValueError, IndexError):
            continue

        # 각 책에 대해 반복합니다.
        for i in range(1, num_books + 1):
            try:
                book_line = sys.stdin.readline().split()
                if not book_line: continue

                book_width = int(book_line[0])
                label_text = book_line[1]
            except (ValueError, IndexError):
                continue

            # 가로 라벨에 필요한 총 너비를 계산합니다.
            # (텍스트 너비) + (앞뒤 여백 2mm)
            required_horizontal_width = (len(label_text) * font_width) + 2

            # 책의 너비와 비교하여 방향을 결정합니다.
            if required_horizontal_width <= book_width:
                orientation = "horizontal"
            else:
                orientation = "vertical"
            
            # --- 수정된 부분 2: 책 정보 출력 형식 변경 (콜론 제거) ---
            print(f"Book {i} {orientation}")

# 함수 실행
solve_library_labels()