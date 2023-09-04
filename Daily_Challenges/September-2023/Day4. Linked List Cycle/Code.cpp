/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
       
       set<ListNode*> s1;
       if(head == NULL){
           return false;
       }
       while(head->next != NULL){
           if(s1.find(head) == s1.end()){
               s1.insert(head);
           }
           else{
               return true;
           }
           head = head->next;
       }
       return false;
        

        
    }
};
