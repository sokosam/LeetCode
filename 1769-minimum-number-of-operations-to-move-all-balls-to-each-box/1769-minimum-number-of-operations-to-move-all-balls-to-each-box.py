class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = 0
        curr = 0

        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            ans[i] += curr
            if boxes[i] == '1':
                left += 1
            curr += left
        
        right = 0
        curr =0

        for i in range(len(boxes) - 1, -1, -1):
            ans[i] += curr
            if boxes[i] == '1':
                right +=1
            curr += right
        return ans