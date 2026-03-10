from typing import List

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         result = 0
#
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) == k:
#                     result += 1
#
#         return result
#
# # sum(i ~ j) = prefix[j] - prefix[i-1]
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         result = 0
#         prefix_sum = [nums[0]]
#
#         for i in range(1, len(nums)):
#             prefix_sum.append(prefix_sum[i - 1] + nums[i])
#
#         for i in range(len(prefix_sum)):
#             if prefix_sum[i] == k:
#                 result += 1
#             for j in range(i + 1, len(prefix_sum)):
#                 # print(f"{i}~{j}까지의 구간합: {prefix_sum[j] - prefix_sum[i]}")
#                 if prefix_sum[j] - prefix_sum[i] == k:
#                     result += 1
#
#         return result

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix = 0
        prefix_sum = {}

        for i in range(len(nums)):
            prefix += nums[i] # 1. 현재 nums[i]의 값을 누적합에 더한다.
            wanted = prefix - k # 2. 찾아야 하는 값 계산

            # print(f"현재 누적합이 {prefix}일 때, {wanted}가 딕셔너리에 있는지 검사")
            if wanted == 0: # 현재 누적합이 k인 경우
                result += 1
            if wanted in prefix_sum:
                result += prefix_sum[wanted]

            # 3. wanted를 찾아본 후, 현재 누적합도 딕셔너리에 저장
            prefix_sum[prefix] = prefix_sum.get(prefix, 0) + 1 # 없으면 값 저장, 있으면 누적
            # print(f"현재 딕셔너리: {prefix_sum}")

        return result

print(Solution.subarraySum(Solution(), [1,1,1], 2)) # 2
print(Solution.subarraySum(Solution(), [1,2,3], 3)) # 2
print(Solution.subarraySum(Solution(), [1], 0)) # 0
print(Solution.subarraySum(Solution(), [0,0,0,0,0,0,0,0,0,0], 0)) # 0