# 1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        result = 0

        # instead of nesting for loops, keep track of the nums 
        # in a dict for quick lookups
        for num in nums:
            count = nums_dict.get(k-num, 0)
            # number DOES have a compliment:
            # take from dict and increment result
            if count >= 1: 
                nums_dict.update({k-num: count - 1})
                result += 1
            # number DOES NOT have a compliment:
            # add it to dict for later
            else:
                nums_dict.update({num: nums_dict.get(num, 0) + 1})

        return result

"""
first attempt brute force code that works but is bad:
=====================================================
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        i, j = 0, 1
        while i < len(nums): # array will change size as elements are removed
            if i != j and nums[i] + nums[j] == k: 
                # equals k -> remove elements, reset j to i + 1 if possible
                result += 1
                del nums[i]
                del nums[j - 1]
                if i + 1 < len(nums):
                    j = i + 1
            else: 
                # not equals k -> advance j until we get a hit (will reset to
                # i + 1) or we reach the end (will advance i and reset j)
                if j < len(nums) - 1:
                    j += 1
                else:
                    # j has reached the end, advance i and reset j
                    # since nothing can be added to it to make k
                    i += 1
                    if i + 1 < len(nums):
                        j = i + 1
        return result
"""