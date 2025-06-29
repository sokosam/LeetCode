class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = [[-1,-1] for _ in range(26)]

        for idx, i in enumerate(s):
            index = ord(i) - ord('a')
            intervals[index][1] = idx
            if intervals[index][0] < 0:
                intervals[index][0] = idx

        cleaned = []
        for interval in intervals:
            if interval[0] != -1:
                cleaned.append(interval)
        cleaned.sort(key = lambda x : x[0])

        ans = []
        current = cleaned[0]
        for i in range(1, len(cleaned)):
            if cleaned[i][0] <= current[1]:
                current[1] = max(current[1], cleaned[i][1])
            else:
                ans.append(current[1] + 1)
                current = cleaned[i]
        ans.append(current[1] + 1)
        for i in range(len(ans) -1, 0, -1):
            ans[i] = ans[i] - ans[i-1]
        return ans
