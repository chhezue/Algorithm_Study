def find_alphabet_occurrence_array(string):
    # 알파벳별 빈도수를 저장하기 위해 0으로 초기화된 배열을 만듦.
    alphabet_occurred_array = [0] * 26

    for char in string:
        if char.isalpha(): # 알파벳인지 아닌지 검사
            alphabet_occurred_array[ord(char) - ord('a')] += 1 # 해당 문자를 인덱스로 치환

    return alphabet_occurred_array

def summarize_string(input_str):
    occurrence_array = find_alphabet_occurrence_array(input_str)
    result = ""

    for i in range(len(occurrence_array)):
        if occurrence_array[i] != 0:
            result += chr(i + ord("a")) + str(occurrence_array[i]) + "/"

    return result[:-1]


print(summarize_string("abc")) # a1/b1/c1
print(summarize_string("aaabbbc")) # a3/b3/c1
print(summarize_string("abbbc")) # a1/b3/c1
print(summarize_string("ahhhhz")) # a1/h4/z1
print(summarize_string("acccdeee")) # a1/c3/d1/e3