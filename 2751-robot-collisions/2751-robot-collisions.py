class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[ positions[i], healths[i], directions[i]] for i in range(len(positions))]

        robots.sort(key = lambda x :x[0])


        s = []
        survived = []
        for i in robots:
            position, health, direction = i

            if direction == "L":
                if not s:
                    survived.append([position , health])
                else:
                    while s:
                        r_pos, r_hp = s.pop()
                        if r_hp == health:
                            health = 0
                            break
                        elif r_hp > health:
                            s.append([r_pos,r_hp - 1])
                            break
                        else:
                            health -=1
                    if not s and health > 0:
                        survived.append([position , health])
            else:
                s.append([position, health])

        survived.extend(s)
        survived = { i[0] : i[1] for i in survived}
        sorted_survived = []
        for i in range(len(positions)):
            if positions[i] in survived:
                sorted_survived.append(survived[positions[i]])
        return sorted_survived