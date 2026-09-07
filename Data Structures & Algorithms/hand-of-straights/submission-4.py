class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        numgroups = len(hand) // groupSize
        groups = []
        for _ in range(numgroups):
            groups.append([])
        hand.sort()

        # 1 2 2 3 3 4 4 5

        d = 0
        group_finished = -1
        for i in range(len(hand)):
            if i == 0:
                groups[0].append(hand[i])
                if len(groups[0]) == groupSize:
                    group_finished = 0
                continue

            if hand[i] == hand[i-1]:
                d = max((d + 1) % numgroups, group_finished + 1)
            else:
                d = group_finished + 1

            if hand[i] in groups[d]:
                return False

            if len(groups[d]) > 0 and hand[i] != groups[d][-1] + 1:
                return False

            groups[d].append(hand[i])
            if len(groups[d]) == groupSize:
                group_finished = d

        # print(groups)

        return True

            
