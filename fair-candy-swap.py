class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalAlice = sum(aliceSizes)
        totalBob = sum(bobSizes)
        targetTotal = (totalAlice + totalBob)//2
        for i in aliceSizes:
            j = i+(targetTotal - totalAlice)
            if j in bobSizes:
                return [i,j]
        