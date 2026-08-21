class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s_cand = sorted(candidates)
        result = []

        def is_part(lists, lst):

            freq_l = {}
            for l in lst:
                if l not in freq_l:
                    freq_l[l] = 0
                freq_l[l] += 1

            for source in lists:
                freq_s = {}
                for s in source:
                    if s not in freq_s:
                        freq_s[s] = 0
                    freq_s[s] += 1
                
                if freq_l == freq_s:
                    return True
            
            return False



        def dfs(ind, path, total):
            if total == target:
                if not is_part(result, path):
                    result.append(path)
                return

            if total > target:
                return

            if ind >= len(candidates):
                return

            curr = candidates[ind]
            dfs(ind + 1, path + [curr], total + curr)

            # skip duplicates
            i = ind + 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, path, total)

        dfs(0, [], 0)
        return result
