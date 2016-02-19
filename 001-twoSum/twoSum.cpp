#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> result; 
            for(int i=1; i<nums.size(); i++) {
                for(int j=0; j<i; j++) {
                    if (nums[i] + nums[j] == target) {
                        result.push_back(j);
                        result.push_back(i);
                        return result;
                    }
                }
            }
            return result;
        }
};
