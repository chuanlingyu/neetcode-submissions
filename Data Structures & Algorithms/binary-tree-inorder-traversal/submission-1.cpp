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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) return vector<int>{};
        vector<int> output{};
        stack<TreeNode*> track{};
        track.push(root); 

        while (root->left != nullptr) {
            track.push(root->left);
            root = root->left;
        }

        while (!track.empty()) {
            TreeNode* tmp{track.top()};
            output.push_back(tmp->val);
            track.pop();

            tmp = tmp->right;
            if (tmp != nullptr) {
                track.push(tmp);
                while (tmp->left != nullptr) {
                    track.push(tmp->left);
                    tmp = tmp->left;
                }
            }
        }

        return output;
    }
};