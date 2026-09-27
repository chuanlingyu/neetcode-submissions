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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> output{};
        if (!root) return output;

        queue<TreeNode*> track;
        track.push(root);

        while (!track.empty()) {
            vector<int> level{};
            int size{static_cast<int>(track.size())};

            for (int i{}; i < size; i++) {
                TreeNode* front{track.front()};
                level.push_back(front->val);

                if (front -> left) track.push(front -> left);
                if (front -> right) track.push(front -> right);
                track.pop();
            }

            output.push_back(level);
        }

        return output;
    }
};
