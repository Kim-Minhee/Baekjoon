# 함수
def check(lst):
  s = ''.join([str(i) for i in lst])
  for n in '0123456789':
    if n not in s:
      return False
  return True

while 1:
  try:
    # 입력
    N = int(input())

    # 풀이
    seq, k = [N], 1
    while 1:
      chk = check(seq)
      if chk:
        # 출력
        print(k)
        break
      else:
        k += 1
        seq.append(k*N)
  except:
    break