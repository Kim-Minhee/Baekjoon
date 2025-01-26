N, k = map(int, input().split())
X = list(map(int, input().split()))

X.sort(reverse=True)
x_dict, r = {}, int()
for x in X:
  if x in x_dict:
    x_dict[x] += 1
  else:
    x_dict[x] = 1
  if sum(x_dict.values())<=k:
    r = x
  else:
    break

print(r)