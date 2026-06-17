class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        if self.freq(s) == self.freq(t):
            return True
        else:
            return False
    def freq(self,nums):
        seen = {}
        for i in nums:
            seen[i]= seen.get(i,0) + 1
        return seen