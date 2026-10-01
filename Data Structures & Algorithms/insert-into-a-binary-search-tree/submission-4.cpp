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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* curr{root};
        TreeNode* parent{};

        if (!curr) return new TreeNode{val};

        while (curr) {
            parent = curr;
            if (val < curr->val) {
                curr = curr -> left;
            } else {
                curr = curr -> right;
            }
        }

        TreeNode* result{new TreeNode{val}};
        if (val < parent -> val) {
            parent -> left = result;
        } else {
            parent -> right = result;
        }

        return root;
    }
};