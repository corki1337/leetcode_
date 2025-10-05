class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int w = nums.size();
        for(int i = 0; i < w; i++){
            for(int j = i+1; j < w; j++){
                if(target == nums[i] + nums[j]){
                    vector<int> wynik = {i, j};
                    return wynik;
                }
            }
        }
        return {};
    }
};