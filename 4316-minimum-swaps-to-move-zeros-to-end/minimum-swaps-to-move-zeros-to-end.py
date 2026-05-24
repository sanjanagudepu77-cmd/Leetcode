class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        non_zero = [x for x in nums if x != 0]
        k = len(non_zero)
        swaps = 0
        for i in range(k):
            if nums[i] == 0:
                swaps += 1
        return swaps