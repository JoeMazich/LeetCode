#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> compliments;
            
            for (int i = 0; i < nums.size(); ++i ){
                
                int compliment = target - nums[i];
                
                auto it = find(compliments.begin(), compliments.end(), compliment);
                if(  it != compliments.end() ) {
                    
                    int ci = it - compliments.begin();
                    return vector<int> {i, ci};
                    
                } else {
                    
                    compliments.insert(compliments.begin() + i, nums[i]);
                    
                }
            }
            
            return nums;
        }
};