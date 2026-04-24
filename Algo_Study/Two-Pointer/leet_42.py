from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                # 현재 벽 >= 왼쪽 벽의 최댓값이라면 max를 갱신해야 물이 고인다.
                if height[left] >= left_max:
                    left_max = height[left]
                # 현재 벽이 max보다 낮으면 그 차이만큼 물이 고인다.
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,0,3,2,5])) # 9