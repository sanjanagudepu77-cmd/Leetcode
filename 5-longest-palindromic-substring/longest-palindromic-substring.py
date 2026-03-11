class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        '''longest = ""
        for r in range(n):
            l = 0   
            while l <= r:
                substring = s[l:r+1]
                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring
                l += 1
        return longest'''
        longest=""
        for i in range(n):
            for j in range(i,n):
                substring=s[i:j+1]
                if substring==substring[::-1]:
                    if len(substring)>len(longest):
                        longest=substring
        return longest

       