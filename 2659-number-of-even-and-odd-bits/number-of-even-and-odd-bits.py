class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary=bin(n)[2:]
        even=0
        odd=0
        ind=0
        for i in range(len(binary)-1,-1,-1):
            if binary[i]=='1':
                if ind%2==0:
                  even+=1
                else:
                  odd+=1
            ind+=1
        return[even,odd]

        