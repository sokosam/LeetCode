import bisect
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        horizontal = {}
        vertical = {}
        foundZero = False
        for obstacle in obstacles:
            if obstacle == [0,0]:
                foundZero = True
                continue
            if obstacle[0] not in vertical:
                vertical[obstacle[0]] = [obstacle[1]]
            else:
                bisect.insort_left(vertical[obstacle[0]] ,obstacle[1])
            if obstacle[1] not in horizontal:
                horizontal[obstacle[1]] = [obstacle[0]]
            else:
                bisect.insort_left(horizontal[obstacle[1]] ,obstacle[0])

        posX, posY = 0, 0
        ans = 0
        # 1 = north , 2 = east, 3 = south, 4 =west
        direction = 1

        for command in commands:
            if command < 0:
                if command == -1:
                    direction += 1
                    if direction >=5: direction = 1
                else:
                    direction -= 1
                    if direction <= 0: direction = 4
            else:
                match direction:
                    case 1:
                        if posX in vertical:
                            arr = vertical[posX]
                            i = bisect_left(arr, posY)
                            if i >= len(arr):
                                posY += command
                            else:
                                block = arr[i]
                                if posY + command >= block:
                                    posY = block - 1
                                else:
                                    posY += command
                        else:
                            posY += command
                    case 2:
                        if posY in horizontal:
                            arr = horizontal[posY]
                            i = bisect_left(arr, posX)
                            if i >= len(arr):
                                posX += command
                            else:
                                block = arr[i]
                                if posX + command >= block:
                                    posX = block - 1
                                else:
                                    posX += command
                        else:
                            posX += command
                    case 3:
                        if posX in vertical:
                            arr = vertical[posX]
                            i = bisect_right(arr, posY)  - 1
                            if i == -1:
                                posY -= command
                            else:
                                block = arr[i]
                                if posY - command <= block:
                                    posY = block + 1
                                else:
                                    posY -= command
                        else:
                            posY -= command
                    case 4:
                        if posY in horizontal:
                            arr = horizontal[posY]
                            i = bisect_right(arr, posX) -1 
                            if i == -1:
                                posX -= command
                            else:
                                block = arr[i]
                                if posX - command <= block:
                                    posX = block + 1
                                else:
                                    posX -= command
                        else:
                            posX -= command
                ans = max(ans, posX**2 + posY**2)
            if foundZero:
                if 0 not in vertical:
                    vertical[0] = [0]
                else:
                    bisect.insort_left(vertical[0] ,0)
                if 0 not in horizontal:
                    horizontal[0] = [0]
                else:
                    bisect.insort_left(vertical[0] ,0)
                foundZero = False
        return ans
