class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        result = set()
        globalState = {}

        def dfs(start, r, c, rows, cols, path):

            if globalState[start]["isPacific"] and globalState[start]["isAtlantic"]:
                result.add(start)
                return

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if path:
                if heights[r][c] > heights[path[-1][0]][path[-1][1]]:
                    return

            if (r, c) in path:
                return

            curr_path = path + [(r, c)]

            if r == 0 or c == 0:
                globalState[start]["isPacific"] = True

            if r == rows-1 or c==cols-1:
                globalState[start]["isAtlantic"] = True

            if (r, c) in globalState:
                if globalState[(r,c)]["isPacific"]:
                    globalState[start]["isPacific"] = True
                if globalState[(r,c)]["isAtlantic"]:
                    globalState[start]["isAtlantic"] = True

            dfs(start, r+1, c, rows, cols, curr_path)
            dfs(start, r-1, c, rows, cols, curr_path)
            dfs(start, r, c-1, rows, cols, curr_path)
            dfs(start, r, c+1, rows, cols, curr_path)

        
        rows = len(heights)
        cols = len(heights[0])

        for r in range(rows):
            for c in range(cols):
                globalState[(r,c)] = {"isPacific": False, "isAtlantic": False}
                dfs((r,c), r, c, rows, cols, [])

        return list(result)