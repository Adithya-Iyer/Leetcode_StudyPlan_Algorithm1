class Solution(object):
    #DISCLAIMER: UNORIGINAL APPROACH
    def helper(self, nums, l, r):
        while (l<r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.helper(nums, 0, n-1)
        self.helper(nums, 0, k-1)
        self.helper(nums, k, n-1)