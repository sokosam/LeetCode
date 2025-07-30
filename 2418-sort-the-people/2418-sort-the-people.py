class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new = [[heights[i],names[i]] for i in range(len(names))]
        new.sort(key = lambda x : x[0], reverse=True)
        new = [i[1] for i in new]
        return new