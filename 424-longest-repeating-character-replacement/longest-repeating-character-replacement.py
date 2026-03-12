class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''ans=0  #tle
        n=len(s)
        for i in range(n):
            mf=0
            freq=[0]*26
            for j in range(i,n):
                idx=ord(s[j])-ord('A')
                freq[idx]+=1
                mf=max(mf,freq[idx])
                if(j-i+1)-mf<=k:
                    ans=max(ans,j-i+1)
        return ans'''
        ans=0
        n=len(s)
        mf=0
        freq={}
        i=0
        for j in range(n):
            ch=s[j]
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
            mf=max(mf,freq[ch])
            while(j-i+1)-mf>k:
                freq[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans

        