class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.m = {}
        self.taskToId = {}
        self.tasks = [[-i[2], -i[1], i[0]]  for i in tasks]
        for i in self.tasks:
            self.taskToId[i[1]] = i[2]
            self.m[i[1]] = i[0]
        heapq.heapify(self.tasks)
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.m[-taskId] = -priority
        self.taskToId[-taskId] = userId

        heapq.heappush(self.tasks, [-priority, -taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.m[-taskId] = -newPriority
        heapq.heappush(self.tasks, [-newPriority, -taskId, self.taskToId[-taskId]])

    def rmv(self, taskId: int) -> None:
       del self.taskToId[-taskId]
       del self.m[-taskId]
        

    def execTop(self) -> int:
        while self.tasks:
            curr = heapq.heappop(self.tasks)
            priority = curr[0]
            taskId = curr[1]
            userId = curr[2]
            if taskId not in self.m or taskId not in self.taskToId:
                continue
            if self.taskToId[taskId] != userId:
                continue
            if priority != self.m[taskId]:
                continue
            else:
                del self.m[taskId]
                del self.taskToId[taskId]
                return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()