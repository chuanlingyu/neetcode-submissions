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
        if (root == nullptr) return output;
        stack<TreeNode*> track{};
        track.push(root);
        while (!track.empty()) {
            TreeNode* tmp{track.top()};
            track.pop();

            output.push_back(tmp->val);
            if (tmp->right != nullptr) track.push(tmp->right);
            if (tmp->left != nullptr) track.push(tmp->left);
        }

        return output;
    }
};