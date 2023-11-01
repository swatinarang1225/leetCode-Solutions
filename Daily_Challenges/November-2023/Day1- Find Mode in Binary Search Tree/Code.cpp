/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void InorderTraversal( struct TreeNode* root, vector<int>& inorder){
        if(root == NULL){
            return;
        }

        InorderTraversal(root->left,inorder);

        inorder.push_back(root->val);

        InorderTraversal(root->right,inorder);
    }

    vector<int> findMode(TreeNode* root) {

        vector<int> inorder;
        vector<int> ans;
        
        //pushing data into inorder traversal form
        InorderTraversal(root,inorder);

        int maximum = INT_MIN;
        map<int,int> mp;

        for(auto val: inorder){
            mp[val]++;

            maximum = max(mp[val],maximum);
        }

        for(auto x : mp){
            if(x.second == maximum){
                ans.push_back(x.first);
            }
        }

        return ans;
        
    }
};
