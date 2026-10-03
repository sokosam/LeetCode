class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        par = [i for i in range(len(s))]
        sets = [{i} for i in s]

        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        def merge(a,b):
            parent1 = find(a)
            parent2 = find(b)

            if parent1 < parent2:
                par[parent2] = parent1
                sets[parent1].update(sets[parent2])

            else:
                par[parent1] = parent2
                sets[parent2].update(sets[parent1]) 

        for pair in pairs:
            merge(pair[0], pair[1])

        groupings = defaultdict(list)
        for index in range(len(par)):
            find(index)
            groupings[par[index]].append((index, s[index]))

        ans = [0]*len(s)
        for parent, group in groupings.items():
            group.sort(key= lambda x : x[1])
            indexes = sorted([i[0] for i in group])
            for i in range(len(indexes)):
                ans[indexes[i]] = group[i][1]
        # print(groupings)
        
        return "".join(ans)




        