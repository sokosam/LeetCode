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
                        row = curr[0]
                        col = curr[1]
                        distance = curr[2]
                        if rooms[row][col] == 0 or rooms[row][col] == -1 or (row,col) in seen:
                            continue
                        if distance < rooms[row][col]:
                            rooms[row][col] = distance
                        
                        seen.add((row,col))
                        if row -1 >= 0:
                            queue.append([row - 1, col, distance + 1])
                        if row + 1 < len(rooms):
                            queue.append([row + 1, col, distance + 1])
                        if col - 1 >= 0:
                            queue.append([row, col -1, distance + 1])
                        if col + 1 < len(rooms[0]):
                            queue.append([row, col + 1, distance + 1])
            
            

            