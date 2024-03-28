class Solution(object):
    """
    https://leetcode.com/problems/first-missing-positive/
    """

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        for i in nums:
            if abs(i) <= len(nums):
                nums[abs(i) - 1] = -abs(nums[abs(i) - 1])

        return next((idx + 1 for idx, v in enumerate(nums) if v > 0), len(nums) + 1)


print(Solution().firstMissingPositive([3, 4, -1, 1]))
