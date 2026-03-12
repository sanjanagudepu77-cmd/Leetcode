class Solution:
    def isValid(self, s: str) -> bool:
        '''st=[]
        for i in s:
            if i in"({[":
                st.append(i)
            else:
                if not st:
                    return False
                top=st.pop()
                if i==')' and top!='(':
                    return False
                if i==']' and top!='[':
                    return False   
                if i=='}' and top!='{':
                    return False 
        return not st  '''
        st=[]
        map={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in map:
                if st:
                   top=st.pop()
                else:
                    top='#'
                if map[ch]!=top:
                    return False
            else:
                st.append(ch)
        return not st
            
