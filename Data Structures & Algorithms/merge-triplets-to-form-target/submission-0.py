class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # idea if the triplet includes that number 
        # in the index
        # just take max of all
        # and see the final output

        # but what if there is more than one possibility?

        ta, tb, tc = target
        ma, mb, mc = 0, 0, 0

        for a,b,c in triplets:
            if a != ta and b != tb and c != tc:
                continue

            if a == ta and b == tb and c == tc:
                return True
            
            if a == ta:
                if b > tb and c > tc:
                    continue

            if b == tb:
                if a > ta and c > tc:
                    continue

            if c == tc:
                if a > ta and b > tb:
                    continue

            ma, mb, mc = max(a, ma), max(b, mb), max(c, mc)


        return ta == ma and tb == mb and tc == mc

            
