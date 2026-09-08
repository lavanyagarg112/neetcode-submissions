class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        boundaries = {}

        for i in range(len(s)):
            ch = s[i]
            boundaries[ch] = i

        result = [0]
        curr_left = 0
        curr_right = 0

        for i in range(len(s)):
            ch = s[i]
            if i <= curr_right:
                curr_right = max(curr_right, boundaries[ch])
                result[-1] = curr_right - curr_left + 1
            else:
                curr_left = i
                curr_right = boundaries[ch]
                result.append(curr_right - curr_left + 1)

        return result


            