class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''n=len(ratings)
        candies=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        return sum(candies)'''
        n=len(ratings)  #mountain greed algorithm
        sumi=1
        i=1
        while i<n:
            if ratings[i]==ratings[i-1]:
              sumi+=1
              i+=1
              continue
            peak=1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                sumi+=peak
                i+=1
            down=1
            while i<n and ratings[i]<ratings[i-1]:
                sumi+=down
                i+=1
                down+=1
            if down>peak:
                sumi+=down-peak
        return sumi
        


        