from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # 집이 하나인 경우
        if n == 1:
            return nums[0]

        # 초기 값 설정
        dp = [0] * n
        # 집이 하나인 경우
        dp[0] = nums[0]
        # 집이 두 개인 경우, 인접한 집은 약탈할 수 없으므로 돈이 더 많은 집을 약탈한다.
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # max(현재 집은 약탈하지 않고 이전 집만 약탈하는 경우, 2번째 전 집과 현재 집을 약탈하는 경우)
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

s = Solution()
print(s.rob([1,2,3,1])) # 4
print(s.rob([2,7,9,3,1])) # 12