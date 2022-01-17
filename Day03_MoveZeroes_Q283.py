class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zc = 0
        i = 0
        for n in nums:
            if (n==0):
                zc+=1
            else:
                nums[i] = n
                i+=1
        for j in range(zc):
            nums[i] = 0
            i+=1