class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        distinct = set()
        for i in nums:
            if i not in distinct:
                distinct.add(i)
            else :
                return True
        return False
        # return len(set(nums)) < len(nums) -->single line pass for length based hashset
    
print(Solution().containsDuplicate([1,3,5,7,9,1]))