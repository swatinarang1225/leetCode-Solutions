class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_concat = "".join(word1)
        word2_concat = "".join(word2)
        if word1_concat == word2_concat:
            return True
        else:
            return False
        
