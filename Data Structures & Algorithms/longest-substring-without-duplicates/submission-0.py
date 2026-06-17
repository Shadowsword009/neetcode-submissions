class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        maxl = 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[left])
                left+=1
            res.add(s[r])
            maxl = max(maxl,r-left+1)
        return maxl






        