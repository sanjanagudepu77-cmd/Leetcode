class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        curr = 0
        max_sum = 0
        for i in range(k):
            curr += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        if len(freq) == k:
            max_sum = curr
        for i in range(k, len(nums)):
            left = nums[i-k]
            freq[left] -= 1
            curr -= left
            if freq[left] == 0:
                del freq[left]
            right = nums[i]
            curr += right
            freq[right] = freq.get(right, 0) + 1

            if len(freq) == k:
                max_sum = max(max_sum, curr)

        return max_sum


