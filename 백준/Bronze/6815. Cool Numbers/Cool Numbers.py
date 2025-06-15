# GPT 4o
A = int(input())
B = int(input())

count = 0
i = 1
while True:
    sixth = i ** 6
    if sixth > B:
        break
    if sixth >= A:
        count += 1
    i += 1

print(count)