# GPT 5
import sys

def encode_binary(s: str) -> str:
    # s는 빈 문자열이 아님이 보장되어야 함
    res = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            res.append(str(count))
            res.append(prev)
            prev = ch
            count = 1
    # 마지막 구간 추가
    res.append(str(count))
    res.append(prev)
    return "".join(res)

def main():
    for raw in sys.stdin:
        line = raw.strip()
        if line == "0":
            break
        if line == "":
            # 빈 줄은 무시
            continue
        # 안전하게 인코딩
        print(encode_binary(line))

if __name__ == "__main__":
    main()