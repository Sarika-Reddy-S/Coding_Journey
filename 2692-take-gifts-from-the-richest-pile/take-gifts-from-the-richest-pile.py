import heapq
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        gift=[-x for x in gifts]
        heapq.heapify(gift)
        for _ in range(k):
            max_ele=-heapq.heappop(gift)
            rem=int(math.sqrt(max_ele))
            heapq.heappush(gift,-rem)
        return -sum(gift)