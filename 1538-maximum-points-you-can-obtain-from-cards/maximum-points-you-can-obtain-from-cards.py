class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''ml=0
        n=len(cardPoints)
        for i in range(k+1):
            ls=0
            rs=0
            for l in range(i):
                ls+=cardPoints[l]
            for r in range(k-i):
                rs+=cardPoints[n-1-r]
            ml=max(ml,ls+rs)
        return ml'''
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        ts=sum(cardPoints)
        windowsize=n-k
        windowsum=sum(cardPoints[:windowsize])
        min_w_sum=windowsum
        for i in range(windowsize,n):
            windowsum+=cardPoints[i]-cardPoints[i-windowsize]
            min_w_sum=min(min_w_sum,windowsum)
        return ts-min_w_sum
                
        
        