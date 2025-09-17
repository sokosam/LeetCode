class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.cuisines = {}
        for i in range(len(foods)):
            self.foods[foods[i]] = [-ratings[i], cuisines[i]]
            if cuisines[i] not in self.cuisines:
                self.cuisines[cuisines[i]] = [[-ratings[i], foods[i]]]
            else:
                heapq.heappush(self.cuisines[cuisines[i]],[-ratings[i], foods[i]] )

    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food][0] = -newRating

        heapq.heappush(self.cuisines[self.foods[food][1]],[self.foods[food][0], food])

    def highestRated(self, cuisine: str) -> str:
        
        heap = self.cuisines[cuisine]

        while heap[0][0] != self.foods[heap[0][1]][0]:
            heapq.heappop(heap)
        return heap[0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)