# 3727. Maximum Alternating Sum of Squares

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_sq = list()
        # preprocessing each element
        for num in nums:
            nums_sq.append(num ** 2)

        nums_sq.sort()
        # sum of right-half bigger numbers minus the sum of the left-half smaller numbers
        return sum(nums_sq[(len(nums)//2):len(nums)]) - sum(nums_sq[0:(len(nums)//2)])