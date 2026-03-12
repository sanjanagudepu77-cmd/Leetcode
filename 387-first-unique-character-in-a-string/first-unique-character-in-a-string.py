class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1'''#only 105/107 test cases passed
                            
        dic={}
        for i in range(len(s)):
            char=s[i]
            if char not in dic:
                dic[char]=1
            else:
                dic[char]=-1
                                              
        for j in range(len(s)):
            is_unique=s[j]
            if dic[is_unique]==1:
                return j
        return -1
        