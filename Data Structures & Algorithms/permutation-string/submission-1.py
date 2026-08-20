class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # apparently O(1) space since max 26 alphabets
        
        n = len(s1)

        if len(s2) < n:
            return False

        s1_freq = {}
        curr_freq = {}
        left = 0

        for s in s1:
            if s not in s1_freq:
                s1_freq[s] = 0
            s1_freq[s] += 1

        for s in s2[:n]:
            if s not in curr_freq:
                curr_freq[s] = 0
            curr_freq[s] += 1

        if s1_freq == curr_freq:
            return True

        for i in range(n, len(s2)):
            curr = s2[i]
            prev = s2[left]
            curr_freq[prev] -= 1
            if curr_freq[prev] == 0:
                curr_freq.pop(prev)

            left += 1
            if curr not in curr_freq:
                curr_freq[curr] = 0
            curr_freq[curr] += 1

            if s1_freq == curr_freq:
                return True
            

        return False
