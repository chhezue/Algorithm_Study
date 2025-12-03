from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, value = stack.pop() # 73일 때 (1, 74)가 꺼내짐.
                result[idx] = i - idx

            stack.append((i, temp)) # (인덱스, 값)

        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]