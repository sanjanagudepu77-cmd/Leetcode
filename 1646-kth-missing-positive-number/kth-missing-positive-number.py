class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        l,h=0,n-1
        while l<=h:
            mid=(l+h)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                h=mid-1
        return k+h+1
        