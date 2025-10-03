class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def getConnected(stone):
                    nonlocal seen
                    seen.add(tuple(stone))
                    q = deque()
                    q.append(stone)
                    curr = 0
                    while q:
                        curr +=1
                        stone = q.popleft()
                        for newStone in stoneCols[stone[1]]:
                            if newStone not in seen:
                                seen.add(newStone)
                                q.append(newStone)
                        for newStone in stoneRows[stone[0]]:
                            if newStone not in seen:
                                seen.add(newStone)
                                q.append(newStone)
                    return curr -1
        stoneCols = defaultdict(list)
        stoneRows = defaultdict(list)

        seen = set()

        for stone in stones:
            stoneCols[stone[1]].append(tuple(stone))
            stoneRows[stone[0]].append(tuple(stone))
        
        ans = 0

        for stone in stones:
            if tuple(stone) not in seen:
                ans += getConnected(stone)
       
        return ans