class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq={}
        for i in nums1:
            for j in nums2:
                s = i + j
                if s in freq:
                    freq[s] += 1
                else:
                    freq[s] = 1

        ans = 0
        for k in nums3:
            for l in nums4:
                target = -(k + l)
                if target in freq:
                    ans += freq[target]

        return ans