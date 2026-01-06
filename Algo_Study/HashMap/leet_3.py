class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_len = 0

        for i, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char] + 1) # 중복되는 문자열 다음으로 시작점 이동

            last_seen[char] = i  # (해당 문자열, 그 문자열이 마지막에 나온 인덱스)
            max_len = max(max_len, i - start + 1) # 반복문이 끝난 이후에도 체크
            print(f"i={i}, char={char}, start={start}, last_seen={last_seen}, max_len={max_len}")

        return max_len

# print(Solution.lengthOfLongestSubstring(Solution(), "abcabcbb")) # 3
# print(Solution.lengthOfLongestSubstring(Solution(), "bbbbb")) # 1
# print(Solution.lengthOfLongestSubstring(Solution(), "pwwkew")) # 3
# print(Solution.lengthOfLongestSubstring(Solution(), "dvdf")) # 3
print(Solution.lengthOfLongestSubstring(Solution(), "abba")) # 3