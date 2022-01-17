class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lol = 0
        n = len(s)
        for i in range(n):
            ll = [s[i]]
            for j in range(i+1, n):
                c = s[j]
                if c in ll:
                    break
                else:
                    ll.append(c)
            l = len(ll)
            if (lol < l):
                lol = l
            if (lol==(n-i)):
                return lol
        return lol