class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = {}
        for i in nums:
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1

        import heapq as hq
        heap = []
        result = []
        for num, count in tmp.items():
            if len(heap) >= k:
                if count >= heap[0][0]:
                    hq.heapreplace(heap, (count, num))
            else:
                hq.heappush(heap, (count, num))
        while heap:
            result.append(hq.heappop(heap)[1])
        return result