from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = 1

        for n in nums_dict:
            max_len = 1
            # 시작점이 되기 위한 조건: 수열의 더 작은 값이 없어야 함.
            if n - 1 not in nums_dict: # 이제 n은 시작점이 된다.
                while n + 1 in nums_dict:
                    n += 1
                    max_len += 1

            result = max(result, max_len)

        return result