// Completed on: 8/18/2023
// Submission: https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1024978277/
// Time Complexity: O(n)
// Space Complexity: O(n) 


#include <windows.h>
#include <climits>

using namespace std;

 struct TreeNode {
    int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

class Solution {
public:
    int omax = INT_MIN;
    int maxPathSum(TreeNode* root) {
        if(!root) return 0;
        rootSums(root);
        return omax;
    }
    int rootSums(TreeNode* root)
    {
        if(!root) return INT_MIN;
        int leftSum = rootSums(root->left);
        int rightSum = rootSums(root->right);
        int sum = root ->val;
        omax = max(sum,omax);
        if(rightSum > 0 && leftSum > 0)
        {
            int branchMax = leftSum + rightSum + sum;
            omax = max(omax,branchMax);
            return sum + max(leftSum, rightSum);

        }
        else if(leftSum > 0 || rightSum > 0)
        {
            int corPath = max(leftSum,rightSum);
            omax = max(corPath+ sum, omax);
            omax = max(corPath,omax);
            return sum + corPath;
        }
        return sum;
    }
};