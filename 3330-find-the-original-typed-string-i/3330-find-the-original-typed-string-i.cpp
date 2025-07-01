class Solution {
public:
    int possibleStringCount(string word) {
        char prev = ' ';
        int ans = 0;
        for (int i =0; i < word.length(); i ++){
            if (prev == word[i]){
                ans ++;
            }
            prev = word[i];
        }
        return ans + 1;
    }
};