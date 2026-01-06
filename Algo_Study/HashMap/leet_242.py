from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 기본 구현: 시간 복잡도 O(n^2)
        # if len(s) >= len(t):
        #     for char in s:  # 더 긴 문자열을 기준으로 검사
        #         if s.count(char) != t.count(char):
        #             return False
        #     return True
        # else:
        #     for char in t:  # 더 긴 문자열을 기준으로 검사
        #         if s.count(char) != t.count(char):
        #             return False
        #     return True

        # 2. 정렬 구현: 시간 복잡도 O(nlogn)
        # return sorted(s) == sorted(t)

        # 3. 딕셔너리 구현: 시간 복잡도 O(n)
        return Counter(s) == Counter(t)


print(Solution.isAnagram(Solution(), "anagram", "nagaram"))
print(Solution.isAnagram(Solution(), "rat", "car"))
print(Solution.isAnagram(Solution(), "a", "ab"))