class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1'''
        sum_s = 0
        sum_t = 0
        for ch in s:
            sum_s += ord(ch)
        for ch in t:
            sum_t += ord(ch)
        return chr(sum_t - sum_s)

        