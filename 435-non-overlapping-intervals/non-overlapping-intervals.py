class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''n=len(intervals)
        p=0
        c=1
        for i in range(1,n):
           if intervals[i][0]>=intervals[p][1]:
              p=i
              c+=1
        return n-c'''
        ends=[]
        for s,e in intervals:
            ends.append((e,s))
        ends.sort()
        c=0
        le=ends[0][0]
        for e,s in ends[1:]:
            if s<le:
                c+=1
            else:
                le=e
        return c
        

        




        