from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0 # 왼쪽에서 가장 높은 벽
        right_max = 0 # 오른쪽에서 가장 높은 벽
        water = 0

        while left < right:
            # current 위치에 따라서 left_max와 right_max를 변형하며 처리해야 한다.
            # print("현재 left:", left, "right:", right, "current:", current)
            # print("현재 left 높이:", height[left], "현재 right 높이:", height[right])
            # print("현재 누적된 물의 양:", water)

            # 오른쪽의 벽 높이가 더 높다면, 왼쪽만 고려하면 됨.
            if height[left] < height[right]:
                if height[left] >= left_max: # 기존의 left_max보다 큰 경우
                    left_max = height[left] # left_max 갱신
                else:
                    water += left_max - height[left]
                left += 1 # 오른쪽으로 좁힘.
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1 # 왼쪽으로 좁힘.

        return water

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))