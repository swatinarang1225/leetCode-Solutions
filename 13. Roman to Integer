class Solution:   
    
    def romanToInt(self, s: str) -> int:
        value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        i = 0
        
        while(i<len(s)):
            s1 = value[s[i]]
            
            if (i+1<len(s)):
                s2 = value[s[i+1]]
                
                if s1 >=s2:
                    res = res + s1
                    i = i+1
                else:
                    res = res + s2-s1
                    i = i+2
            else:
                res = res + s1
                i = i+1
        return res
                
