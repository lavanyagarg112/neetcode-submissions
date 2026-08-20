class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []



        def dfs(ind, path, total):
            if total == target:
                # if path not in result and not is_part(result, path):
                # no need cause sorted
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
