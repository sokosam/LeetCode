class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = sum(wall[0])
        m = defaultdict(int)

        for edge in wall:
            curr = 0
            for i in edge:
                curr += i
                if curr != width:
                    m[curr] += 1
        return len(wall) - max(m.values()) if len(m) != 0 else len(wall)

