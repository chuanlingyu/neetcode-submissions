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
        vector<vector<int>> output;
        if (!root) return output;

        queue<TreeNode*> track{};
        track.push(root);

        while (!track.empty()) {
            size_t size{track.size()};
            vector<int> count{};

            for (size_t i{}; i < size; i++) {
                TreeNode* front{track.front()};
                count.push_back(front->val);

                track.pop();

                if (front -> left) track.push(front -> left);
                if (front -> right) track.push(front -> right);
            }

            output.push_back(count);
        }

        return output;
    }
};
