def find_max_occurred_alphabet(string):
    # 알파벳별 빈도수를 저장하기 위해 0으로 초기화된 배열을 만듦.
    alphabet_occurred_array = [0] * 26

    for char in string:
        if char.isalpha(): # 알파벳인지 아닌지 검사
            alphabet_occurred_array[ord(char) - ord('a')] += 1 # 해당 문자를 인덱스로 치환

    max_index = alphabet_occurred_array.index(max(alphabet_occurred_array))

    return chr(max_index + ord("a"))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))