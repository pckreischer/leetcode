# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)

        current = 1
        for i in range(len(answer)):
            answer[i] *= current
            current *= nums[i]

        current = 1
        for i in reversed(range(len(answer))):
            answer[i] *= current
            current *= nums[i]

        return answer