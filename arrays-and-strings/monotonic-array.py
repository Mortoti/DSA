class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                increasing = False
            elif nums[i]< nums[i+1]:
                decreasing = False
            
        return decreasing or increasing


                 
