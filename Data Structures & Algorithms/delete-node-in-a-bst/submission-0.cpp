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
        while (curr != nullptr) {
            if (curr -> val == key) break;
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

    void delete0(TreeNode*& curr, TreeNode*& parent, TreeNode*& root) {
        if (parent == nullptr) {
            root = nullptr;
        } else if (curr == parent -> left) {
            parent -> left = nullptr;
        } else {
            parent -> right = nullptr;
        }

        delete curr;
    }

    void delete1(TreeNode*& curr, TreeNode*& parent, TreeNode*& root) {
        TreeNode* child{curr -> left? curr -> left : curr -> right};

        if (parent == nullptr) {
            root = child;
        } else if (curr == parent -> left) {
            parent -> left = child;
        } else {
            parent -> right = child;
        }

        delete curr;
    }

    void delete2(TreeNode*& curr) {
        TreeNode* iop{curr->left};
        int oldVal{curr->val};
        while (iop -> right) {
            iop = iop -> right;
        } 

        swap(curr->val, iop -> val);
        curr->left = deleteNode(curr -> left, oldVal);
    }
};