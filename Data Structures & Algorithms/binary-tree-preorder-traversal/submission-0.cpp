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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> output{};
        helper(output, root);
        return output;
    }

    void helper(vector<int>& output, TreeNode* root) {
        if (root == nullptr) return;
        output.push_back(root->val);
        helper(output, root->left);
        helper(output, root->right);
    }
};