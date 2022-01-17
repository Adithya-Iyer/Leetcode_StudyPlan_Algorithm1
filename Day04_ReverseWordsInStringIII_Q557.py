class Solution:
    def reverseString(self, s: str) -> str:
        """
        Do not return anything, modify s in-place instead.
        """
        r = []
        l = len(s)
        for i in range(l):
            r.append(s[l-i-1])
        #print(''.join(r))
        return (''.join(r))
    
    def reverseWords(self, s: str) -> str:
        rev = []
        words = s.split()
        for w in words:
            rev.append(self.reverseString(w))
        return (' '.join(rev))