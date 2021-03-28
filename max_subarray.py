class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_
        
