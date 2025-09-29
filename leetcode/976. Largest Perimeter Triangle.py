class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        f = True
        for i in range(len(nums)-2):
            c = nums[i]
            a = nums[i + 1]
            b = nums[i + 2]
            if c < a + b:
                return c + a + b
                f = False
                break
        if f:
            return 0
