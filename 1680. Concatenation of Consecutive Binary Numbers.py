class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        def decTobin(num):
            c =  bin((num))
            return c[2:]
        
        for i in range(1,n+1):
            res += str(decTobin(i))
        
        return(int(res,2)%( (10**9)+7))  
        
            
           
