class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(lambda: 0)
        
        s = 0
        count = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                count += 1
            if (s-k) in hash_map:
                count += hash_map[s-k]
            hash_map[s] += 1
            
        return count
                
