/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> nodemap;
        if(head == NULL){
            return NULL;
        }

        Node* newhead = new Node(head->val);
        nodemap[head] = newhead;

        Node* current = head->next;
        Node* newCurrent = newhead;

        while(current != NULL){
            newCurrent->next = new Node(current->val);
            newCurrent = newCurrent->next;
            nodemap[current] = newCurrent;
            current = current->next;
        }

        current = head;
        newCurrent = newhead;

        while(current != NULL){
            if(current->random != NULL){
                newCurrent->random = nodemap[current->random];

            }
            current = current->next;
            newCurrent = newCurrent->next;

        }
        return newhead;
    }
};
