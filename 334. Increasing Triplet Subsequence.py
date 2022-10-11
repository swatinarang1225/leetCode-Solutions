class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i,j=float("inf"),float("inf")
        if len(nums)<3:
            return False
        for k in nums:
            if k<=i:
                i=k
            elif k<=j:
                j=k
            else:
                return True
        return False
