class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        
        quo, rem = divmod(c[0], 2)
        if rem: return[]
        ans = [0]*quo   

        for n in sorted(c.keys()):
            if c[n] > c[2*n]: return []
            c[2*n]-= c[n]
            ans.extend([n]*c[n])
            

        return ans
        
