class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        output = []
        i = 1
        n = len(nums)
        for key,value in nums_dict.items():
            if value > 1:
                output.append(key)
        while(i<n+1):
            if i not in nums_dict:
                output.append(i)
            i+=1

        return output
                
            
        
