class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s_cand = sorted(candidates)
        result = []

        def dfs(ind, path, total):
            if total == target:
                if path not in result:
                    result.append(path)
                return

            if total > target:
                return

            if ind >= len(candidates):
                return

            curr = candidates[ind]
            dfs(ind + 1, path + [curr], total + curr)
            dfs(ind + 1, path, total)

        dfs(0, [], 0)
        return result
