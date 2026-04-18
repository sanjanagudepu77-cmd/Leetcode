class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        def helper(x, rev):
            if x == 0:
                return rev
            return helper(x // 10, rev * 10 + x % 10)
        rev = helper(x, 0)
        if rev > 2**31 - 1:
            return 0
        return sign * rev