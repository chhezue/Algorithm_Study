def find_not_repeating_first_character(string):
    # 1. string에서 알파벳의 빈도 수를 찾는다.
    # 2. 빈도수가 1인 알파벳들 중, string에서 먼저 선언된 알파벳을 찾는다.

    occurrence_array = find_alphabet_occurrence_array(string)
    not_repeating_alphabet_array = []

    for i in range(len(occurrence_array)):
        if occurrence_array[i] == 1:
            not_repeating_alphabet_array.append(chr(i + ord("a"))) # 해당 알파벳

    for char in string:
        if char in not_repeating_alphabet_array:
            return char

    return "_"

def find_alphabet_occurrence_array(string):
    # 알파벳별 빈도수를 저장하기 위해 0으로 초기화된 배열을 만듦.
    alphabet_occurred_array = [0] * 26

    for char in string:
        if char.isalpha(): # 알파벳인지 아닌지 검사
            alphabet_occurred_array[ord(char) - ord('a')] += 1 # 해당 문자를 인덱스로 치환

    return alphabet_occurred_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))