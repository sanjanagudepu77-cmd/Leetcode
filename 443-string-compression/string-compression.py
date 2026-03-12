class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i=0
        n=len(chars)
        while i<n:
            count=1
            while i+1<n and chars[i]==chars[i+1]:
                count+=1
                i+=1
            s+=chars[i]
            if count>1:
                s+=str(count)
            i+=1
        for j in range(len(s)):
            chars[j]=s[j]
        return len(s)
            
