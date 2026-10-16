# 3723. Maximize Sum of Squares of Digits

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # early exit for no answer solutions
        # (all 9s wouldn't be enough)
        if sum > (9 * num): return ''

        # greedy approach: get as many 9s as we can
        result = [9] * (sum // 9)

        # after we append as many 9s we can, add what remains
        if len(result) < num:
            result.append(sum % 9)

        # calculate how many 0s to tack on
        num -= len(result)
        result.extend([0] * num)

        return ''.join(str(item) for item in result)