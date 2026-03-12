class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits'''
        carry = 1   
        for i in range(len(digits) - 1, -1, -1):
            new_val = digits[i] + carry
            digits[i] = new_val % 10
            carry = new_val // 10
        if carry:
            digits=[1]+digits
        return digits