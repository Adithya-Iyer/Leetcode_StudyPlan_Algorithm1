class Solution:
    def hammingWeight(self, n: int) -> int:
        bs = format(n, "b")
        n=0
        for ch in bs:
            if (ch=='1'):
                n+=1
        return n