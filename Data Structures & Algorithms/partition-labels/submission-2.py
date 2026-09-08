class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # greedy: just keep updating the right boundary
        # while the letters are within the current boundary
        # Time: O(n)
        # Space: O(1)
        
        boundaries = {}

        for i in range(len(s)):
            ch = s[i]
            boundaries[ch] = i

        result = [0]
        curr_left = 0
        curr_right = 0

        for i in range(len(s)):
            ch = s[i]

            # if my i is less than the right we have right now
            # then it has to be considered to consider the right 
            # boundary
            # and we keep updating the result
            if i <= curr_right:
                curr_right = max(curr_right, boundaries[ch])
                result[-1] = curr_right - curr_left + 1

            # if my i > right boundary, we can now start a new
            # boundary! 
            else:
                curr_left = i
                curr_right = boundaries[ch]
                result.append(curr_right - curr_left + 1)

        return result


            