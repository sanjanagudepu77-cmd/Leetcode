class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def generate(ind, subset, ans, nums):
            if ind == len(nums):
                ans.append(subset.copy())
                return

        # TAKE
            subset.append(nums[ind])
            generate(ind + 1, subset, ans, nums)
            subset.pop()

        # NOT TAKE (skip duplicates)
            next_ind = ind + 1
            while next_ind < len(nums) and nums[next_ind] == nums[ind]:
                next_ind += 1
            generate(next_ind, subset, ans, nums)
        ans = []
        generate(0, [], ans, nums)
        return ans
     

        