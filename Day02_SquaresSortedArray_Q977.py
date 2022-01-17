class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #TRIVIAL APPROACH
        for i in range(len(nums)):
            n = nums[i]
            nums[i] = n*n
        nums.sort()
        return nums
