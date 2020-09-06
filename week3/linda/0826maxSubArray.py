class Solution:
    def maxSubArray(self, nums) -> int:
        max = nums[0]
        pre = nums[0]
        for i in range(1,len(nums)):
            cur = max(pre,0)+nums[i]
            pre = cur
            if cur>max:
                max = cur
        return max