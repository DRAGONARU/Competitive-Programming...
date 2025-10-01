class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        a = len(nums)
        while a != 1:
            for i in range(a - 1):
                nums.append((nums[i] + nums[i + 1]) % 10)
            for i in range(a):
                nums.pop(0)
            a = len(nums)
        return nums[0]
