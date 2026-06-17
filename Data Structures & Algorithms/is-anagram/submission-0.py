class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def anagram(s):
            seen = {}
            for i in s:
                if i in seen:
                    seen[i] += 1
                else:
                    seen[i] = 1
            return seen

        if anagram(s) == anagram(t):
            return True
        return False