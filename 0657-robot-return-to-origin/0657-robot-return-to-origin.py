class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves)% 2 == 1:
            return False

        count = Counter(moves)

        if "U" in count or "D" in count:
            if "U" not in count or "D" not in count:
                return False
            if count['U'] != count["D"]:
                return False
        if "L" in count or "R" in count:
            if "L" not in count or "R" not in count:
                return False
            if  count["R"] != count["L"]:
                return False
        return True