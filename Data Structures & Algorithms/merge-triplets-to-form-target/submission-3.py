class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # idea if the triplet includes that number 
        # in the index
        # just take max of all
        # and see the final output

        # but what if there is more than one possibility?

        ta, tb, tc = target

        # since target >= 1
        ma, mb, mc = 0, 0, 0

        for a,b,c in triplets:

            # if exact triplet is there then true
            if a == ta and b == tb and c == tc:
                return True

            # if none of them match, ignore
            if a != ta and b != tb and c != tc:
                continue
            
            # if atleast one of them matches, but any other is
            # more than target -> ignore
            if a > ta or b > tb or c > tc:
                continue

            # otherwise consider and take max
            ma, mb, mc = max(a, ma), max(b, mb), max(c, mc)


        return ta == ma and tb == mb and tc == mc

            
