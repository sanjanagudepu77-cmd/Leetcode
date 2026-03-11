class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num ** 0.5
        if sqrt % 2 == 0 or sqrt % 2 == 1:
            return True
        return False
        