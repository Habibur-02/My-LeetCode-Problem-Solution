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
    bool is_identical(TreeNode* root1, TreeNode* root2)
  {
      if(root2==NULL || root1== NULL)
      return root1==root2;
      
      bool left_identical= is_identical(root1->left, root2->left);
      bool right_identical= is_identical(root1->right, root2->right);
      return left_identical && right_identical && root2->val== root1->val;
      
      
      
  }
  
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        TreeNode* root1=subRoot;
        if(root==NULL || root1== NULL)
        return root==root1;
      if(root->val==root1->val && is_identical(root, root1))
      {
          return true;
      }
      
      bool left= isSubtree(root->left, root1);
      bool right= isSubtree(root->right, root1);
      return left || right;
    }
};
