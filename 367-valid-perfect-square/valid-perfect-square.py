class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''sqrt = num ** 0.5
        if sqrt % 2 == 0 or sqrt % 2 == 1:
            return True
        return False'''
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
               return True
            elif mid * mid < num:
               left = mid + 1
            else:
               right = mid - 1
        return False
        