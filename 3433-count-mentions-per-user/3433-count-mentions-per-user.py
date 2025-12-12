class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        

        users = [0]*numberOfUsers
        online = [True for _ in range(numberOfUsers)]
        events = [[0 if i[0] == "OFFLINE" else 1, int(i[1]), i[2] ] for i in events]
        online_date = defaultdict(int)



        events.sort(key = lambda x : (x[1], x[0])) 
        # print(events)

        q = deque()
        alls = 0

        for event in events:
            message, timestamp, mentions = event

            if message == 0:
                user_id = int(mentions)
                online[user_id] = False
                online_date[user_id] = int(timestamp) + 60
                q.append([int(timestamp) + 60, user_id])
            else:
                while q and q[0][0] <= int(timestamp):
                    curr = q.popleft()
                    time, user_id = curr
                    if time == online_date[user_id]:
                        online[user_id] = True
                
                if mentions == "ALL":
                    alls +=1
                elif mentions == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            users[i] +=1
                else:
                    ids = mentions.split(" ")
                    for user_id in ids:
                        index = int(user_id[2:])
                        users[index] += 1

        users = [i + alls for i in users ]
        return users

