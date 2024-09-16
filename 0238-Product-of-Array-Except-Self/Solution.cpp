// Completed on: 7/13/2023
// Submission: https://leetcode.com/problems/product-of-array-except-self/submissions/993750291/
// Time Complexity: O(n^2)
// Space Complexity: O(n) 
//   k : Number of distinct elements


#include <vector>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size());
        output[0] = 1;
        int right = 1;
        for (int i = 1; i < nums.size(); i++ )
        {
            output[i] = output[i - 1] * nums[i - 1];
        }
        for(int i = nums.size() - 1; i >=0; i--)
        {
            output[i] *= right;
            right *= nums[i];
        }
    return output;
    }
    
};
