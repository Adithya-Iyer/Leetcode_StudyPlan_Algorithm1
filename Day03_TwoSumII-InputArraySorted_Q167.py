class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumDict = {}
        for i in range(len(numbers)):
            n = numbers[i]
            if n in sumDict:
                return ([sumDict[n]+1,i+1])
            sumDict[(target-n)] = i
        return ([0,0])