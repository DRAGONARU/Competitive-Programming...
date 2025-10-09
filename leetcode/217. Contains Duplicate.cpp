class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, unsigned> unique;
    for (int i = 0; i < nums.size(); i++) {
	    if (unique.contains(nums[i]) == false) {
		    unique[nums[i]] = 0;
	    }
	    else {
		    return true;
	    }
    }
    return false;
    }
};
