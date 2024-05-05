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
    void deleteNode(ListNode* node) {

        ListNode *tail = node;

        while(tail!= NULL){
            tail->val = tail->next->val;
            if(tail->next->next == NULL){
                tail->next = NULL;
                
            }
            tail = tail->next;
        }
        
    }
};
