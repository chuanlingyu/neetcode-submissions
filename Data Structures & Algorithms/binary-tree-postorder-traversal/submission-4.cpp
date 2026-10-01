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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> output{};
        if (!root) return output;

        stack<TreeNode*> track1{};
        stack<TreeNode*> track2{};
        track1.push(root);

        while (!track1.empty()) {
            TreeNode* top{track1.top()};
            track1.pop();
            track2.push(top);

            if (top -> left) track1.push(top -> left);
            if (top -> right) track1.push(top -> right);
        }

        while (!track2.empty()) {
            output.push_back(track2.top() -> val);
            track2.pop();
        }

        return output;
    }
};