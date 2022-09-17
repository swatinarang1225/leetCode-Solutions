class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = nums1[0:m]
        new = new+nums2
        new.sort() 
        for i in range(0,len(nums1)):
            nums1[i] = new[i]
        print(nums1)
        
