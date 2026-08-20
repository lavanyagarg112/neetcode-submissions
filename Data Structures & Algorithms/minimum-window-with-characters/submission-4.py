class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        original_freq = {}
        for ch in t:
            if ch not in original_freq:
                original_freq[ch] = 0
            original_freq[ch] += 1

        
        left = 0
        chars = {}

        have = 0
        need = len(original_freq)

        result = -1
        length = -1

        for right in range(len(s)):

            # add to chars if in t
            if s[right] not in chars:
                chars[s[right]] = 0
            chars[s[right]] += 1

            if s[right] in original_freq and chars[s[right]] == original_freq[s[right]]:
                have += 1

            # check validity of window until get invalid window
            while have == need:
                if result == -1 or right - left + 1 < length:
                    result = [left, right]
                    length = right - left + 1
                
                chars[s[left]] -= 1
                if s[left] in original_freq and chars[s[left]] < original_freq[s[left]]:
                    have -= 1
                left += 1
                
        if result == -1:
            return ""

        return s[result[0]: result[1] + 1]




