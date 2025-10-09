# GPT 5
import sys

def decrypt(line: str) -> str:
    res = []
    for ch in line:
        if 'A' <= ch <= 'Z':
            v = ord(ch) - 5
            if v < ord('A'):
                v += 26
            res.append(chr(v))
        else:
            res.append(ch)
    return ''.join(res)

def main():
    for raw in sys.stdin:
        token = raw.strip()
        if token == "ENDOFINPUT":
            break
        if token == "START":
            cipher = sys.stdin.readline().rstrip('\n')  # 메시지 (공백 보존)
            end = sys.stdin.readline().strip()  # should be "END"
            # 복호화 및 출력
            print(decrypt(cipher))

if __name__ == "__main__":
    main()