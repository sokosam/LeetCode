class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        
        
        int z = 0;
        for (int i = 0; i < nums.size(); i++){
            if(nums[i] == key or nums[i] == -key){
                z = i;
                while (z >= 0 && nums[z] > 0 && z >= i - k ){
                    if (nums[z] > 0){
                    nums[z] = -nums[z];

                    }
                    z --;
                }
                z = i + 1;
                while (z < nums.size() && z <= i + k){
                    if (nums[z] > 0){
                    nums[z] = -nums[z];

                    }
                    z ++;
                }
            }
        }

        int ptr = 0;
        for (int i = 0; i < nums.size(); i ++){
            if (nums[i] < 0){
                nums[ptr] = i;
                ptr++;
            }
        }
        while(nums.size() > ptr){
            nums.pop_back();
        }

        return nums;
    }
};