from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] # 전체 결과
        path = []

        def dfs(start):
            if len(path) == k:
                result.append(path[:])

            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return result

s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))