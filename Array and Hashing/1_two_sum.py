class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevPass = {}
        for indx,num in enumerate(nums):
            diff = target - num 
            if diff in prevPass:
                return [prevPass[diff],indx]
            prevPass[num] = indx
        
    
print(Solution().twoSum([2,5,7,11],10))