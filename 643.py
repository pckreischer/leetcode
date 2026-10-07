# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum = 0
        for i in range(k):
            sum += nums[i]

        max = sum / k

        for right in range(k, len(nums)):
            left = right - k
            sum += nums[right] - nums[left]
            avg = sum / k
            if avg > max:
                max = avg

        return max
        
            