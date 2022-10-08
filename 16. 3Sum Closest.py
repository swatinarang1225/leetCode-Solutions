class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:    
        nums.sort()
        sums=0
        closest=sum(nums[0:3])
        if closest>target:
            return closest
        closest=sum(nums[-3:])
        if closest<target:
            return closest
        for i in range(len(nums)):
            b=i+1
            c=len(nums)-1
            while b<c:
                sums=nums[i]+nums[b]+nums[c]
                if abs(target-sums)<abs(target-closest):
                    closest = sums
                elif sums<target:
                    b+=1               
                else:
                    c-=1
                    
        return closest
