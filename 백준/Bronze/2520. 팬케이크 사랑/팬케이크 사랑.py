dough = [8/16, 8/16, 4/16, 1/16, 9/16]
topping = [1, 30, 25, 10]

# 입력
T = int(input())
for _ in range(T):
  input()
  DOUGH = list(map(int, input().split()))
  TOPPING = list(map(int, input().split()))

  # 풀이
  x = list()
  for i in range(5):
    x.append(DOUGH[i]/dough[i])
  possible_dough = int(min(x))

  possible_topping = 0
  for i in range(4):
    possible_topping += TOPPING[i]//topping[i]
  
  # 출력
  print(min(possible_dough, possible_topping))