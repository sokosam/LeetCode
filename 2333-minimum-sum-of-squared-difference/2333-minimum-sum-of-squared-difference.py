class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        nums = [abs(nums1[i] - abs(nums2[i])) for i in range(len(nums1))]

        k = k1 + k2

        c = Counter(nums)

        heap = [(-key,val) for key,val in c.items()]
        heapify(heap)
        while k > 0:
            val, count = heappop(heap)
            val = -val

            to_next = 0
            if count >= k:
                to_next = k
            else:
                to_next = count

            if len(heap) > 0 and  -(val - 1) == heap[0][0]:
                _,next_count = heappop(heap)
                heappush(heap,( -(val - 1), next_count + to_next))
            else:
                heappush(heap, (-(val - 1), to_next))

            if count > to_next:
                heappush(heap, (-val, count - to_next))

            k -= to_next

        return sum([(key**2)*count if key <= 0 else 0 for key,count in heap])


