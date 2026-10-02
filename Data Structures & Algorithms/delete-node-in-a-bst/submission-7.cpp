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
        TreeNode* par{};

        while (curr) {
            if (curr -> val == key) break;

            par = curr;
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
            delete1(curr, par, root);
        } else {
            delete0(curr, par, root);
        }

        return root;
    }

private:
    void delete0(TreeNode*& curr, TreeNode*& par, TreeNode*& root) {
        if (!par) {
            root = nullptr;
        } else if (curr == par -> left) {
            par -> left = nullptr;
        } else {
            par -> right = nullptr;
        }

        delete curr;
    }

    void delete1(TreeNode*& curr, TreeNode*& par, TreeNode*& root) {
        TreeNode* child {
            curr -> left ?
            curr -> left :
            curr -> right
        };

        if (!par) {
            root = child;
        } else if (curr == par -> left) {
            par -> left = child;
        } else {
            par -> right = child;
        }

        delete curr;
    }

    void delete2(TreeNode*& curr) {
        TreeNode* iop{curr -> left};
        int ori{curr -> val};

        while (iop -> right) {
            iop = iop -> right;
        }

        std::swap(curr -> val, iop -> val);

        curr -> left = deleteNode(curr -> left, ori);
    }
};