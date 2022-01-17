class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<4):
            return n
        f = [1,2,3]
        for i in range(3, n):
            f.append(f[i-1]+f[i-2])
        return f.pop()