'''class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="".join(char.lower() for char in s if char.isalnum())
        b=a[::-1]
        return a==b'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''st = ""
        for ch in s:
            if ch.isalnum():
                st+=ch.lower()
        return st == st[::-1]'''
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
            
        
        