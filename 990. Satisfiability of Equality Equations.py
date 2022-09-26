
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [x for x in range(26)]
        
        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(a,b):
            ua = ufind(a)
            ub = ufind(b)
            
            parent[ua] = ub

            
        for equation in equations:
            if equation[1] == "!":
                continue
            
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            
            uunion(a,b)
        
        for equation in equations:
            if equation[1] != "!":
                continue
            
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            
            if ufind(a) == ufind(b):
                print(1)
                return False
            
        return True
            
        
