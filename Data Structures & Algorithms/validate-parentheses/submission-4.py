class Solution:
    def isValid(self, s: str) -> bool:
        maps = {"]":"[", "}":"{",")":"("}
        stack = []
        for i in s:
            if i in maps:
                if not stack or stack.pop() != maps[i]:
                    return False

                    break
            else:
                stack.append(i)
        return True if not stack else False