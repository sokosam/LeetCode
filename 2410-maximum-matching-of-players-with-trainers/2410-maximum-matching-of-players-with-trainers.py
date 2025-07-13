class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        highest = max(trainers)
        trainers = [-i for i in trainers]
        players = [-i for i in players if i <= highest]
        heapify(players)
        heapify(trainers)
        ans  = 0
        while players and trainers and (players[0] >= trainers[0]):
            ans +=1
            heappop(players)
            heappop(trainers)
        return ans