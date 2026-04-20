from typing import List

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         # 전체 비용이 연료보다 적다면, 한 바퀴를 돌 수 없다는 것을 의미한다.
#         # 반대의 경우에는 한 바퀴를 도는 경우가 무조건 존재함을 의미한다.
#         if sum(gas) < sum(cost):
#             return -1
#
#         # gas[i] - cost[i] < 0 이라면, 시작점이 될 수 없다.
#         diff = []
#         for i in range(len(gas)):
#             diff.append(gas[i] - cost[i])
#         print(diff)
#
#         n = len(gas)
#         start = 0
#
#         while start < n:
#             # 1. 모든 시작점에 대해 for문 실행
#             can_start = True
#             cur_gas = 0
#
#             # 2. 차이가 0보다 작으면 애초에 시작점이 될 수 없으므로 pass
#             if diff[start] < 0:
#                 start += 1
#                 continue
#
#             # 3. 차이가 0보다 크면 시작점 후보 가능
#             for j in range(start, start + n):
#                 idx = j % n  # 원형 순회
#                 cur_gas += diff[idx]
#
#                 if cur_gas < 0:
#                     print(f"시작점 {start}에서 주행하는 도중 연료가 0보다 작아짐. ({cur_gas})")
#                     can_start = False
#                     # 어디서 실패했는지 지점 찾기
#                     # 다음 시작점은 end + 1이어야 한다.
#                     start = j + 1
#                     break
#
#             if can_start:
#                 return start
#
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 전체 비용이 연료보다 적다면, 한 바퀴를 돌 수 없다는 것을 의미한다.
        # 반대의 경우에는 한 바퀴를 도는 경우가 무조건 존재함을 의미한다.
        if sum(gas) < sum(cost):
            return -1

        start_idx = 0
        total_gas = 0

        # 한 바퀴를 도는 경우가 무조건 존재함이 보장됨.
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]

            # 지금까지의 연료의 합이 0보다 작다면, idx를 다음으로 옮김.
            if total_gas < 0:
                start_idx = i + 1
                total_gas = 0

        return start_idx

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1