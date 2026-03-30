class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        # Step 1: Impossible case
        if m * k > n:
            return -1
        # Step 2: Helper function
        def possible(day):
            count = 0
            bouquets = 0
            for num in bloomDay:
                if num <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m
        # Step 3: Binary Search
        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


    
        