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
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* curr{root};
        TreeNode* parent{};

        while (curr) {
            if (curr->val == key) break;
            parent = curr;

            if (key < curr -> val) {
                curr = curr -> left;
            } else {
                curr = curr -> right;
            }
        }

        if (!curr) return root;
        if (curr -> left && curr -> right) {
            delete2(curr);
        } else if (curr -> left || curr -> right) {
            delete1(curr, parent, root);
        } else {
            delete0(curr, parent, root);
        }

        return root;
    }

private:
    void delete0(TreeNode*& curr, TreeNode*& parent, TreeNode*& root) {
        if (!parent) {
            root = nullptr;
        } else if (curr == parent -> left) {
            parent -> left = nullptr;
        } else {
            parent -> right = nullptr;
        }

        delete curr;
    }

    void delete1(TreeNode*& curr, TreeNode*& parent, TreeNode*& root) {
        TreeNode* child{
            curr -> left?
            curr -> left:
            curr -> right
        };

        if (!parent) {
            root = child;
        } else if (parent -> left == curr) {
            parent -> left = child;
        } else {
            parent -> right = child;
        }

        delete curr;
    }

    void delete2(TreeNode*& curr) {
        TreeNode* toSwap{curr->left};
        int val{curr -> val};

        while (toSwap -> right) {
            toSwap = toSwap -> right;
        }

        std::swap(curr -> val, toSwap -> val);
        curr -> left = deleteNode(curr->left, val);
    }
};