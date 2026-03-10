from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_dict = {}

        for item in nums:
            nums_dict[item] = True

        for n in nums_dict:
            max_len = 1

            # 시작점이 되기 위한 조건: 수열의 더 작은 값이 없어야 함.
            if n - 1 not in nums_dict: # 이 조건을 걸면 n이 시작점임을 보장
                while n + 1 in nums_dict: # 딕셔너리 in 연산은 O(1)
                    max_len += 1
                    n += 1
                    # print(f"{n}을 기준으로 {n + 1}이 있으므로 max_len을 늘린다. max_len: {max_len}")

            result = max(result, max_len)

        return result

print(Solution.longestConsecutive(Solution(), [100,4,200,1,3,2]))
print(Solution.longestConsecutive(Solution(), [0,3,7,2,5,8,4,6,0,1]))
print(Solution.longestConsecutive(Solution(), [1,0,1,2]))