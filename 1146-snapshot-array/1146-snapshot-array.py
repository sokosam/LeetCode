

class SnapshotArray:

    def __init__(self, length: int):
        self.track = [{} for _ in range(length)]
        self.total_snaps = 0

    def set(self, index: int, val: int) -> None:
        self.track[index][self.total_snaps ] = val
        
    def snap(self) -> int:
        self.total_snaps +=1
        return self.total_snaps - 1

    def get_max(self, index, snap_id):
        best = -1
        for i in self.track[index].keys():
            if i > best and i <= snap_id:
                best = i
        return best

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.track[index]:
            bid = self.get_max(index,snap_id)
            if bid == -1:
                return 0
            return self.track[index][bid]
        return self.track[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)