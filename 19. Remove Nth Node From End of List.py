# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def delete(head,n):
            temp = prev = head
            count = -1
            if n==0:
                prev = prev.next
            else:
                while(temp):
                    count += 1
                    if count == n-1:
                        temp.next = temp.next.next
                    temp = temp.next
            return prev


        def len(head):
            temp = head;
            count = 0
            while(temp):
                count +=1
                temp = temp.next
            return count
        
        if len(head)!= 1:
            n_from_beg = len(head) - n
            return delete(head,n_from_beg)
        else:
            return None
        

            
            
        
