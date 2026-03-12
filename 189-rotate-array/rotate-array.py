class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n   # to handle k > n

        def rev(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        # Step 1: reverse the whole array
        rev(0, n - 1)
        # Step 2: reverse first k elements
        rev(0, k - 1)
        # Step 3: reverse remaining n-k elements
        rev(k, n - 1)

        