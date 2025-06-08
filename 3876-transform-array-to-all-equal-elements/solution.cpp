class Solution {
public:
    bool canMakeEqual(vector<int>& nums, int k) {
        return canConvert(nums, k, 1) || canConvert(nums, k, -1);
    }

    bool canConvert(vector<int> nums, int k, int target) {
        int ops = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] != target) {
                // Flip nums[i] and nums[i+1]
                nums[i] *= -1;
                nums[i+1] *= -1;
                ops++;
                if (ops > k) return false;
            }
        }
        return nums.back() == target;
    }
};

