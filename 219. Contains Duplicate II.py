class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in index_dict and i - index_dict[num] <= k:
                return True
            index_dict[num] = i
        return False 
        
