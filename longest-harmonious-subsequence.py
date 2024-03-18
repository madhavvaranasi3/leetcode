class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_counts = {}
        for i in nums:
            num_counts[i] = num_counts.get(i,0) + 1
        max_length = 0
        for i in num_counts:
            if i+1 in num_counts:
                max_length = max(max_length , num_counts[i] + num_counts[i+1])
        return max_length