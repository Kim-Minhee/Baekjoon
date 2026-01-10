# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 12791번 Starman 문제 해결 함수
    David Bowie의 앨범 정보를 저장해두고, 질의(S, E)에 해당하는 앨범들을 찾아 출력합니다.
    """
    # 1. David Bowie 앨범 데이터베이스 (연도, 앨범 이름)
    # 문제의 예제 2번 출력을 바탕으로 작성되었습니다.
    albums = [
        (1967, "DavidBowie"),
        (1969, "SpaceOddity"),
        (1970, "TheManWhoSoldTheWorld"),
        (1971, "HunkyDory"),
        (1972, "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"),
        (1973, "AladdinSane"),
        (1973, "PinUps"),
        (1974, "DiamondDogs"),
        (1975, "YoungAmericans"),
        (1976, "StationToStation"),
        (1977, "Low"),
        (1977, "Heroes"),
        (1979, "Lodger"),
        (1980, "ScaryMonstersAndSuperCreeps"),
        (1983, "LetsDance"),
        (1984, "Tonight"),
        (1987, "NeverLetMeDown"),
        (1993, "BlackTieWhiteNoise"),
        (1995, "1.Outside"),
        (1997, "Earthling"),
        (1999, "Hours"),
        (2002, "Heathen"),
        (2003, "Reality"),
        (2013, "TheNextDay"),
        (2016, "BlackStar")
    ]

    try:
        # 첫 줄: 질의의 수 Q
        line = input().strip()
        if not line:
            return
        Q = int(line)

        for _ in range(Q):
            # 질의 S(시작 연도), E(종료 연도)
            query = input().split()
            if not query:
                break
            S, E = map(int, query)
            
            # 2. 조건에 맞는 앨범 필터링
            result = []
            for year, name in albums:
                # S년 1월 1일 ~ E년 12월 31일 사이 발매
                if S <= year <= E:
                    result.append(f"{year} {name}")
            
            # 3. 결과 출력
            # 첫 줄: 앨범 개수
            print(len(result))
            # 이후: 앨범 목록 (있을 경우만)
            for line in result:
                print(line)

    except ValueError:
        pass

if __name__ == "__main__":
    solve()