class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        count = Counter(sentence)
        keys = []
        for key in count.keys():
            keys.append(key)
        if len(keys) == len(alphabets):
            return True
        else:
            return False
        
        
