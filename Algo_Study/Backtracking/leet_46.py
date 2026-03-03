from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # 전체 결과
        path = [] # i = 1 이라면 [1], [1, 2], [1, 3], [1, 2, 3] 이 반환될 것이다.
        visited = [False] * len(nums)

        def dfs(start):
            if len(path) == len(nums):
                result.append(path[:])

            for i in range(len(nums)):
                if visited[i]:
                    continue

                path.append(nums[i])
                visited[i] = True
                dfs(i + 1)
                path.pop()
                visited[i] = False

        dfs(0)
        return result

s = Solution()
print(s.permute([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]