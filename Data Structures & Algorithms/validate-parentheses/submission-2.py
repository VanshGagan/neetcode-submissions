class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                if len(stack) == 0:
                    return False
                if hashmap[char] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                