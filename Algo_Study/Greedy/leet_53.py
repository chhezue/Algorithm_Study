from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

            # 현재 합이 음수가 된다면, 다음 요소가 양수이든 음수이든 (현재 합 + 다음 요소)는 절대 최댓값이 될 수 없다는 것을 의미한다.
            # 그러므로 0으로 초기화하여 이전 값을 버린다. (다음 요소부터 부분 배열을 다시 센다.)
            if cur_sum < 0:
                cur_sum = 0

        return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([1])) # 1
print(s.maxSubArray([5,4,-1,7,8])) # 23