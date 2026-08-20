class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def is_valid(original, freq_map):
            for ch in original:
                if ch not in freq_map or freq_map[ch] < original[ch]:
                    return False
            return True

        
        original_freq = {}
        for ch in t:
            if ch not in original_freq:
                original_freq[ch] = 0
            original_freq[ch] += 1

        
        left = 0
        result = None

        chars = {}
        curr = ""

        while left < len(s) and s[left] not in original_freq:
            left += 1

        for right in range(left, len(s)):

            # add to chars if in t
            if s[right] in original_freq:
                if s[right] not in chars:
                    chars[s[right]] = 0
                chars[s[right]] += 1

            # add to current window
            curr += s[right]

            if s[right] in original_freq:

                # check validity of window until get invalid window
                while is_valid(original_freq, chars):
                    if result == None:
                        result = curr
                    else:
                        result = min(result, curr, key=len)

                    # update left of window
                    chars[s[left]] -= 1
                    left += 1
                    curr = curr[1:]
                    
                    while left < right and s[left] not in original_freq:
                        left += 1
                        curr = curr[1:]
                
        if result == None:
            result = ""
        return result




