# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        temp = head
        count = 0 
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = self.count(head)
        if c == 1:
            return None
        mid = c//2
        i = 0
        temp = head
        while(temp):
            if i == mid-1:
                temp.next = temp.next.next
            i += 1
            temp = temp.next
        return head
                
