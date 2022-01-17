class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """i = 0
        ps = triangle[0][0]
        for ind in range(1, len(triangle)):
            if (triangle[ind][i]>triangle[ind][i+1]):
                i+=1
            ps+=triangle[ind][i]
        return ps"""
        downSums = triangle
        for j in reversed(range(len(triangle)-1)):
            for i in range(j+1):
                downSums[j][i]+=min(downSums[j+1][i], downSums[j+1][i+1])
        return downSums[0][0]