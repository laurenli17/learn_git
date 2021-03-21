from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        nums.sort()
        return nums[len(nums)//2]