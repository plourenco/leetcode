"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""


class Solution(object):

    def trap(self, height):
        water_empty, start_idx = self._trap(height)
        if start_idx is not None:
            water_empty += self._trap(height[start_idx:][::-1])[0]
        return water_empty

    def _trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_idx = None
        max_blocked = 0
        water_blocked = 0
        water_empty = 0
        for idx, val in enumerate(height):
            if start_idx == None:
                if val == 0:
                    continue
                start_idx = idx
                continue
            if val < height[start_idx]:
                water_blocked += val
                if val > max_blocked:
                    max_blocked = val
            else:
                water_empty += height[start_idx] * \
                    (idx - start_idx - 1) - water_blocked
                start_idx = idx
                water_blocked = 0
                max_blocked = 0

        return water_empty, start_idx


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(arr))
