# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        output=[]
        while(point != None):
            if point.val not in output:
                output.append(point.val)
            point = point.next
        output.sort()
        if len(output)!= 0:
            root = temp = ListNode(output[0])
            for i in range(1,len(output)):
                c = ListNode(output[i])
                temp.next = c
                temp = c
            return root
        
