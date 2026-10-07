# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        planted = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check left
                emptyLeft = (i == 0) or (flowerbed[i-1] == 0)
                # check right
                emptyRight = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                if emptyLeft and emptyRight:
                    flowerbed[i] = 1
                    planted += 1

        return planted >= n
            

