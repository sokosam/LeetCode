// Completed on: 7/11/2023
// Submission: https://leetcode.com/problems/contains-duplicate/submissions/991606596/
// Time Complexity: O(n)
// Space Complexity: O(k) 
//   k : Number of distinct elements



#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i ++)
        {
            if(map.find(nums[i]) == map.end())
            {
                map[nums[i]] = nums[i];
            }
            else return true;
        }
        return false;
    }
};