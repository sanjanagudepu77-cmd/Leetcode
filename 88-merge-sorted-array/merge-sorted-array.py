class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=nums1[:m]+nums2
        x.sort()
        nums1[:]=x
        '''for i in range(n):  wrong check it later
            nums1[m+i]=nums2[i]
        tot=m+n
        for i in range(tot):
            for j in range(i+1,tot):
                if nums1[i]>nums1[j]:#bubble sort 
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        return nums1'''

        

        


        