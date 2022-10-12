class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum1 = 0
        print(nums)
        for i in range(0,len(nums)-2): 
            if nums[i] + nums[i+1] > nums[i+2]:
                s = nums[i] + nums[i+1] + nums[i+2]
                if s > sum1:
                    sum1 = s
        return sum1
        
        
