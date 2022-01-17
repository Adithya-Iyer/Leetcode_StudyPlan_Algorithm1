class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        exc = [0]
        inc = [nums[0]]
        for i in range(1, n):
            exc.append(max(exc[i-1], inc[i-1]))
            inc.append(nums[i] + exc[i-1])
        return (max(inc.pop(), exc.pop()))