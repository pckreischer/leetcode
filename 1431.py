# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        most = max(candies)
        result = []

        for kid in candies:
            if kid + extraCandies >= most:
                result.append(True)
            else:
                result.append(False)

        return result