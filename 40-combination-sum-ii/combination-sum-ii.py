class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # ✅ needed for duplicate handling
        def generate(ind, comb, ans, candidates, target):
            if target == 0:
                ans.append(comb.copy())   # ✅ copy
                return
            if target < 0 or ind == len(candidates):
                return
            # ✅ TAKE (move forward, no reuse)
            comb.append(candidates[ind])
            generate(ind + 1, comb, ans, candidates, target - candidates[ind])
            comb.pop()
            # ❗ SKIP duplicates in NOT-TAKE
            next_ind = ind + 1
            while next_ind < len(candidates) and candidates[next_ind] == candidates[ind]:
                next_ind += 1
            # ❌ NOT TAKE
            generate(next_ind, comb, ans, candidates, target)
        ind=0
        ans = []
        comb=[]
        generate(ind,comb, ans, candidates, target)
        return ans
        