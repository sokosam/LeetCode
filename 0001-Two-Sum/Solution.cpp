// Completed on: 9/11/2023
// Submission: https://leetcode.com/problems/two-sum/submissions/1046924412/
// Time Complexity: O(n)
// Space Complexity: O(n) 

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap; 
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }

        return {}; // No solution found
    }
};

// Completed on: 7/6/2023
// Submission: https://leetcode.com/problems/two-sum/submissions/988114245/
// Time Complexity: O(n^2)
// Space Complexity: O(1) 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++)
        {
            for(int k = i + 1; k < nums.size(); k++)
            {
                if(nums.at(i) + nums.at(k) == target) return {i, k};
            }
        }
        return {};
    }
};