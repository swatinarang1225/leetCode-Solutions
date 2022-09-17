class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPal(s):
            if s == s[::-1]:
                return 1
        
        output = []
        backward = {n[::-1]:i for i,n in enumerate(words)} 
        for i, word in enumerate(words):
            
            if word in backward and i!= backward[word]:
                output.append([i, backward[word]])
                    
            if word!='' and isPal(word) and '' in backward:
                    output.append([i,backward['']])
                    output.append([backward[''],i])
                    
            if word!= '':
                for j in range(1,len(word)):
                    pre = word[:j]
                    suf = word[j:]
                    if isPal(word[:j]) and suf in backward:
                        output.append([backward[suf],i])
                    if isPal(word[j:]) and pre in backward:
                        output.append([i,backward[pre]])
                   
                        
                        
        return output
