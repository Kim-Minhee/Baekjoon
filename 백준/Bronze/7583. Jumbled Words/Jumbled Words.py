# GPT 4o
def jumble_word(word):
    if len(word) <= 3:
        return word
    return word[0] + word[1:-1][::-1] + word[-1]

while True:
    line = input()
    if line == "#":
        break
    words = line.split()
    jumbled = [jumble_word(word) for word in words]
    print(" ".join(jumbled))