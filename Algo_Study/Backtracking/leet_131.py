from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def dfs(start):
            if start == len(s):
                result.append(path[:])

            # 현재 start에서 끝 인덱스를 하나씩 늘려가며 조각을 만들어 봄.
            for end in range(start, len(s)):
                # palindrome인 경우에만 dfs 수행 (가지치기)
                substr = s[start:end+1]
                if substr == substr[::-1]:
                    print(f"현재 검사하고 있고, palindrome인 문자열: {substr}")
                    path.append(substr)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result

s = Solution()
print(s.partition("aab"))
print(s.partition("a"))