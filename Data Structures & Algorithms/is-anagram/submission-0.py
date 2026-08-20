class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        def make_hash(string, d):
            for s in string:
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1


        make_hash(s, d1)
        make_hash(t, d2)

        return d1 == d2