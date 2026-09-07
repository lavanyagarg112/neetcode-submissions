class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for h in hand:
            if h not in freq:
                freq[h] = 0
            freq[h] += 1

        hand.sort()

        for h in hand:
            # start by creating the group from the next available
            # small item
            if freq[h]:
                for i in range(h, h + groupSize):
                    if i not in freq or freq[i] == 0:
                        return False
                    freq[i] -= 1
        
        return True

        