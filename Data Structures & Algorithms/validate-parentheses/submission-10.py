class Solution:
    def isValid(self, s: str) -> bool:
        maps = {"{":"}","[":"]","(":")"}
        stack = []
        for i in s:
            if i in maps:
                stack.append(maps[i])
            else:
                if not stack or stack.pop() != i:
                    return False

        return True if not stack else False