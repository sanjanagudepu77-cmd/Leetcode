class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for n in num:
            while st and st[-1]>n and k>0:
              st.pop()
              k-=1
            st.append(n)
        while k>0:
           st.pop()
           k-=1
        res="".join(st).lstrip('0')
        if res:
            return res
        else:
            return "0"
        