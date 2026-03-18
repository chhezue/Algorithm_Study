# 같은 문자가 두 번 이상 등장하지 않는 부분 문자열 중에서 가장 긴 것의 길이를 구하는 것
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        str_set = set()

        while right < len(s): # 가변 크기 윈도우이므로 while문 사용
            # 중복 검사: 늘어난 s[right]가 해시에 있는지 확인
            if s[right] in str_set:
                left += 1
                str_set.remove(s[left - 1])
                # print(dict)
            else:
                max_len = max(max_len, right - left + 1)
                str_set.add(s[right])
                right += 1
                # print(dict)

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # 3
print(s.lengthOfLongestSubstring("bbbbb")) # 1
print(s.lengthOfLongestSubstring("pwwkew")) # 3