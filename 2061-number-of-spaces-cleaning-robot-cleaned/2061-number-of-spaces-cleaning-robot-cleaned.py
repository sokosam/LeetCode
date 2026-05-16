class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        
        if len(room) == 1 and len(room[0]) == 1:
            return 1
        def out_of_bounds(room,curr_x,curr_y, direction):
            dx ,dy = direction
            if dx +curr_x < 0 or dx + curr_x >= len(room):
                return True
            if dy + curr_y < 0 or dy + curr_y >= len(room[0]):
                return True

            new_x = dx + curr_x
            new_y = dy + curr_y

            if room[new_x][new_y] == 1:
                # print(dx,curr_x,dy,curr_y,new_x,new_y,room[new_x][new_y])
                return True
            return False

    
            
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        room_reached = [[[False,False,False,False] for _ in range(len(room[0]))] for _ in range(len(room))]
        count = 0
        curr_x, curr_y = 0,0
        curr_iter = 0

        while True:
            if room_reached[curr_x][curr_y][curr_iter] == True:
                return count
            if not any(room_reached[curr_x][curr_y]):
                count +=1
                # print(curr_x,curr_y,curr_iter,count)

            room_reached[curr_x][curr_y][curr_iter] = True

            c = 0

            while out_of_bounds(room, curr_x, curr_y, dirs[curr_iter]):
                c +=1
                curr_iter = (curr_iter + 1) % 4
                # print(curr_x,curr_y,curr_iter,count)
                if c > 5:
                    return count

            dx,dy = dirs[curr_iter]
            curr_x +=dx
            curr_y +=dy
        return count




