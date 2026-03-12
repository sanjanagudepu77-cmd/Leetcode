class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        wat=0
        while l<r:
            if height[l]<height[r]:
                wat+=max(0,lmax-height[l])
                lmax=max(lmax,height[l])
                l+=1
            else:
                wat+=max(0,rmax-height[r])
                rmax=max(rmax,height[r])
                r-=1
        return wat
        