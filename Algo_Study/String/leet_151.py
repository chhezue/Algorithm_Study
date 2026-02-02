class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split() # 문자열 잘라서 배열로 변환
        reversed_arr = str_arr[::-1] # 배열 뒤집기
        return " ".join(reversed_arr) # 공백으로 join -> 문자열로 반환

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good   example"))