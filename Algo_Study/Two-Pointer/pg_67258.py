def solution(gems):
    answer = [0, 0]
    left = 0
    right = 0
    min_len = float('inf')
    gem_len = len(set(gems))
    # print(gem_len)
    dict = {}

    while right < len(gems): # 가변 크기 윈도우이므로 while문 사용
        dict[gems[right]] = dict.get(gems[right], 0) + 1  # 보석 추가
        right += 1
        # print(dict)

        # 현재 구간에 각 보석이 몇 개 들어있는지 확인
        while gem_len == len(dict.keys()):
            if min_len > right - left + 1:
                min_len = right - left + 1
                answer[0] = left + 1
                answer[1] = right
                # print("answer:", answer)

            # 중복 검사: 늘어난 s[right]가 해시에 있는지 확인
            if gems[left] in dict:
                dict[gems[left]] -= 1
                if dict[gems[left]] == 0:
                    del dict[gems[left]]
                left += 1
                # print("보석 제거:", dict)

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]