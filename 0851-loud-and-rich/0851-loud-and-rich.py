class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        adj = [[] for _ in range(len(quiet))]
        ans = [i for i in range(len(quiet))]
        indir = [0] * len(quiet)

        for wealthier, poorer in richer:
            adj[wealthier].append(poorer)
            indir[poorer] += 1
        

        queue = deque()
        for person in range(len(indir)):
            if indir[person] == 0:
                queue.append(person)

        while queue:
            curr_person = queue.popleft()

            for poorer_person in adj[curr_person]:
                indir[poorer_person] -= 1

                if quiet[ans[curr_person]] < quiet[ans[poorer_person]]:
                    ans[poorer_person] = ans[curr_person]

                if indir[poorer_person] == 0:
                    queue.append(poorer_person)
        return ans