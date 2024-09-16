// Completed on: 15/9/2024
// Submission: https://leetcode.com/problems/valid-palindrome/submissions/1391626737/
// Time Complexity: O(n)
// Space Complexity: O(1) 


#include <string>
using namespace std;

class Solution{
    public:

    bool isPalindrome(string s){
        int left = 0;
        int right = s.length() -1;
        string lowered = "";
        for (int i = 0 ; i < s.length() ; i++){
            lowered += tolower(s[i]);
        }
        s = lowered;
        

        while(left <= right){
            if (!isalnum(s[left]))
            {
                left++;
                continue;
            }
            else if (!isalnum(s[right])){
                right--;
                continue;
            }
            else if (s[left] != s[right]){
                return false;
            }
            left ++;
            right --;
        }
        return true;
    }
};