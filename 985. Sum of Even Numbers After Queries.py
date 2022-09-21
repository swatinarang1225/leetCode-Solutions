class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        sum_initial = sum(filter(lambda x: x%2 == 0, nums))
        
        for val,index in queries:
            if nums[index]%2 != 0:
                nums[index] +=val
            else:
                sum_initial -= nums[index]
                nums[index] += val
            if nums[index]%2 == 0:
                sum_initial += nums[index]
            output.append(sum_initial)
        return output
