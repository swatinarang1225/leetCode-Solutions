from functools import lru_cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)    #cache for function with same params
        def dp(n, target):  
            if n == 1:                  #if there was one dice left 
                return int(target<=k)   #check target less than biggest face in dice (k)
            return sum(dp(n - 1, target - i - 1) for i in range(min(k,target-1)))
        return dp(n, target) % (10 ** 9 + 7)
