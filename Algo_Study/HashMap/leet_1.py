from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            # 1. 숫자를 보면서 필요한 값이 이미 있었는지 확인
            need = target - nums[i]
            if need in nums_dict:
                return [i, nums_dict[need]]

            # 2. 없으면 기록
            nums_dict[nums[i]] = i