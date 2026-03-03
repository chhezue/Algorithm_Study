from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] # 전체 결과
        path = [] # i = 1 이라면 [1], [1, 2], [1, 3], [1, 2, 3] 이 반환될 것이다.

        def dfs(start):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result

s = Solution()
print(s.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(s.subsets([0])) # [[], [0]]