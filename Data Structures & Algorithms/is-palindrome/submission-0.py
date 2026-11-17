class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [char.lower() for char in s if char.isalnum()]
        first = 0
        last = -1
        for i in range(len(lst)):
            if lst[first] == lst[last]:
                first += 1
                last -= 1
            else:
                return False
        return True
            
