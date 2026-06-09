class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: 
                count = count + 1 
        if count == 0 : 
            return False
        else : 
            return True


nums = [1, 2, 3, 4]
sol = Solution()
sol.hasDuplicate(nums)
        