for _ in range(int(input())):
  N = int(input())

  if int(N**(1/3))==(N**(1/3)):
    print(int(N**(1/3))**2 * 6)
  else:
    possible = []
    sum_abc = []

    for a in range(1, N):
      for b in range(1, N//a+1):
        for c in range(1, N//(a*b)+1):
          if a*b*c==N:
            p = sorted([a, b, c])
            if p not in possible:
              possible.append(p)
              sum_abc.append(sum(p))
            break

    min_sum = min(sum_abc)
    min_index = sum_abc.index(min_sum)
    a, b, c = possible[min_index]

    print(2*(a*b + b*c + c*a))