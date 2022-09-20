class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for k in range(n2+1)] for l in range(n1+1)]
        
        result = 0
        for i in range(n1+1):
            for j in range(n2+1):
                if (i==0 or j==0):
                    dp[i][j] = 0
                elif (nums1[i-1] == nums2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result,dp[i][j])
                else:
                    dp[i][j] = 0
        
        
        return result
        
