from collections import defaultdict
class Solution(object):
    def groupAnagrams(self,strs):
        h= defaultdict(list)
        k=""
        ar=[0]*26
        for you in strs:
            s = k.join(sorted(you))
            h[s].append(you)
            
        return sorted(h.values())
        
