# Gemini 2.5 Pro
# 사용자로부터 두 개의 문구를 입력받습니다.
phrase1 = input()
phrase2 = input()

# 1. 각 문구에서 공백을 모두 제거합니다.
processed_phrase1 = phrase1.replace(' ', '')
processed_phrase2 = phrase2.replace(' ', '')

# 2. 공백이 제거된 두 문자열의 문자를 정렬합니다.
#    만약 두 문구가 애너그램 관계라면, 정렬된 결과는 동일해야 합니다.
sorted_chars1 = sorted(processed_phrase1)
sorted_chars2 = sorted(processed_phrase2)

# 3. 정렬된 결과를 비교하여 애너그램 여부를 판별합니다.
if sorted_chars1 == sorted_chars2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")