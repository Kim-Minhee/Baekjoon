n, k = map(int, input().split())

images = []
for _ in range(n):
  pixel = list(map(int, input().split()))
  pixels = []
  for p in pixel:
    for _ in range(k):
      pixels.append(p)
  images.append(pixels)

for image in images:
  for _ in range(k):
    print(*image)