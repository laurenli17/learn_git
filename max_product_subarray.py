class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = float("-inf")
                for num in nums:
                    cur_pro *= num
                    if cur_pro > 0:
                        res = max(res, cur_pro // min_pos)
                        min_pos = min(min_pos, cur_pro)
                    elif cur_pro < 0:
                        if max_neg != float("-inf"):
                            res = max(res, cur_pro // max_neg)
                        else:
                            res = max(res, num)
                        max_neg = max(max_neg, cur_pro)
                    else:
                        cur_pro = 1
                        min_pos = 1
                        max_neg = float("-inf")
                        res = max(res, num)
                return res 

