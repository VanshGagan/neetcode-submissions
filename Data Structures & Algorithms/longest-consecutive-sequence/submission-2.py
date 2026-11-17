class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 1

        nums = set(nums)
        
        if len(nums) == 0:
            return 0
        for num in nums:
            if (num - 1) in nums:
                continue
            elif (num - 1) not in nums:
                local_counter = 1
                x = num
                while x+1 in nums:
                    local_counter += 1
                    x += 1
                if local_counter > counter:
                    counter = local_counter
        return counter