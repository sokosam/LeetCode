from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        queue = deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:

                    if row -1 >= 0:
                        queue.append([row - 1, col,  1])
                    if row + 1 < len(rooms):
                        queue.append([row + 1, col, 1])
                    if col - 1 >= 0:
                        queue.append([row, col -1,  1])
                    if col + 1 < len(rooms[0]):
                        queue.append([row, col + 1, 1])

                    seen = set()
                    while queue:
                        curr = queue.popleft()
                        row2 = curr[0]
                        col2 = curr[1]
                        distance = curr[2]
                        if rooms[row2][col2] == 0 or rooms[row2][col2] == -1 or (row2,col2) in seen:
                            continue
                        if distance < rooms[row2][col2]:
                            rooms[row2][col2] = distance
                        
                        seen.add((row2,col2))
                        if row2 -1 >= 0:
                            queue.append([row2 - 1, col2, distance + 1])
                        if row2 + 1 < len(rooms):
                            queue.append([row2 + 1, col2, distance + 1])
                        if col2 - 1 >= 0:
                            queue.append([row2, col2 - 1, distance + 1])
                        if col2 + 1 < len(rooms[0]):
                            queue.append([row2, col2 + 1, distance + 1])
                        
            
            

    
