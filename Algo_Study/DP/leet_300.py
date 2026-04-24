from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # 원소가 하나인 경우
        if n == 1:
            return 1

        # dp[i]를 "i번째 원소를 마지막으로 포함하는 LIS의 길이"로 정의한다.
        dp = [1] * n
        dp[0] = 1

        if nums[0] >= nums[1]:
            dp[1] = 1
        else:
            dp[1] = 2

        for i in range(2, n):
            for j in range(0, i):
                # 현재 숫자가 직전 숫자보다 클 경우, dp 배열의 길이를 1 증가시킨다.
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(s.lengthOfLIS([0,1,0,3,2,3])) # 4
print(s.lengthOfLIS([7,7,7,7,7,7,7])) # 1