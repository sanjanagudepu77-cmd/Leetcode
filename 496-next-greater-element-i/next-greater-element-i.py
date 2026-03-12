class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nge={}
        r=[]
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            if stack:
               nge[num]=stack[-1] 
            else:
                nge[num]=-1
            stack.append(num)  
        for i in nums1:
            r.append(nge[i])
        return r

            
        
        