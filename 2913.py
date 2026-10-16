# 2913. Subarrays Distinct Element Sum of Squares I

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        left, right = 0, 1
        answer = 0
        while right - left < len(nums) + 1:
            # subset logic
            dist = set(nums[left:right])
            answer += len(dist) ** 2

            # window logic
            # note: needs to be refactored using a sliding window approach
            # still more to cover -> shift window
            if right < len(nums):
                left += 1
                right += 1
            # end of list -> expand window by 1 and start from beginning
            else:
                right = len(nums) - left + 1
                left = 0

        return answer
            

            


