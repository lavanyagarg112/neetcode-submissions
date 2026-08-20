class Solution:
    # time: O(n * log m)

    def canFinish(self, rate, piles, h):

        hours = 0
        for i in range(len(piles)):
            hours += piles[i]//rate
            if piles[i] % rate != 0:
                hours += 1
            if hours > h:
                return False

        return True
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_speed = 1
        max_speed = max(piles)
        ans = max_speed

        while min_speed <= max_speed:
            mid_speed = min_speed + (max_speed - min_speed)//2
            if self.canFinish(mid_speed, piles, h):
                ans = mid_speed
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1

        return ans