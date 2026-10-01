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
        vector<int> output{};
        if (!root) return output;

        stack<TreeNode*> track{};
        track.push(root);

        TreeNode* curr{root};
        while (curr -> left) {
            curr = curr -> left;
            track.push(curr);
        }

        while (!track.empty()) {
            TreeNode* top{track.top()};
            output.push_back(top -> val);
            track.pop();

            if (top -> right) {
                top = top -> right;
                track.push(top);
                while (top -> left) {
                    top = top -> left;
                    track.push(top);
                }
            }
        }

        return output;
    }
};