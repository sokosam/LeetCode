class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groups = [[] for _ in range(500)]


        for index,i in enumerate(groupSizes):

            if len(groups[i]) == 0 or len(groups[i][-1]) == i:
                groups[i].append([index])
            else:
                groups[i][-1].append(index)
        

        ans = []
        for i in groups:
            if len(i) != 0:
                for j in i:
                    ans.append(j)
        return ans
