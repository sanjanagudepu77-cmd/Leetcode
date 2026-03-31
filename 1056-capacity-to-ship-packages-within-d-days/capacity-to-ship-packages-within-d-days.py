class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap):
            d=1
            load=0
            for w in weights:
                if w>cap:
                    return False
                if load+w>cap:
                    d+=1
                    load=w
                else:
                    load+=w
            return d<=days
        l=max(weights)
        h=sum(weights)
        while l<=h:
            mid=(l+h)//2
            if possible(mid):
                h=mid-1
            else:
                l=mid+1
        return l
        