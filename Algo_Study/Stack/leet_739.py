from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]