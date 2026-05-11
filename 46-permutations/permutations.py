class Solution:
    def recurPermute(self, nums, ds, ans, freq):
        # Base condition
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                ds.append(nums[i])
                self.recurPermute(nums, ds, ans, freq)
                ds.pop()
                freq[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        freq = [False] * len(nums)
        self.recurPermute(nums, ds, ans, freq)
        return ans
        