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
    int maxDepth(TreeNode* root) {
        int depth{};
        if (!root) return depth;

        queue<TreeNode*> track{};
        track.push(root);

        while (!track.empty()) {
            size_t size{track.size()};

            for (size_t i{}; i < size; i++) {
                TreeNode* front{track.front()};
                track.pop();

                if (front -> left) track.push(front -> left);
                if (front -> right) track.push(front -> right);
            }

            depth++;
        }

        return depth;
    }
};
