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
    void ans(vector<int> & v, TreeNode* root)
    {
        if(root== NULL) return;
        ans(v, root->left);
        v.push_back(root->val);
        ans(v, root->right);
        
    }
    vector<int> inorderTraversal(TreeNode* root) {
        // if(root == NULL) return;
        vector<int>v;
        ans(v, root);
        return v;

    }
};
