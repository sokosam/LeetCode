class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """

        1 : 1
        2 : 2
        3 : 1,2


        seen = [False]*len(languages)

        adj = [[] for _ in range(len(languages))]
        groups = []

        for i in range(len(languages)):
            check if i is in seen,
                if seen:
                    continue since we dont need to check
                else:
                    run bfs
                    add all items in the bfs to seen
                    and all items to a group

        m = [0]*n
        for group in groups:
            we need to find the langauge that we would need to teach to the least amt of people
            so to do this, we first take the count of each language in each group

            then the total number of people for each language that we need to teach would be
            len(group) - #of individuals that knows the language

            we keep track of this count in a map like m
            and the number with the fewest at the end is the best language
        """

 


        # individuals = len(languages)
        # seen = [False for _ in range(individuals)]
        # adj = [[] for _ in range(individuals)]

        # for i in friendships:
        #     first = i[0] -1
        #     second = i[1] -1
        #     adj[first].append(second)
        #     adj[second].append(first)
        
        
        # groups = []
        
        # q = deque()

        # for i in range(len(seen)):
        #     if not seen[i]:
        #         q.append(i)
        #         newGroup = []
        #         while q:
        #             curr = q.popleft()
        #             seen[curr] = True
        #             newGroup.append(curr)
        #             for k in adj[curr]:
        #                 if not seen[k]:
        #                     q.append(k)
        #                     seen[k] = True
        #         groups.append(newGroup)

        languages = [set(i) for i in languages]
        best = float('inf')
        for i in range(1, 1 + n):
            taught = 0
            taughtIndividuals = [False]*len(languages)
            for friendship in friendships:
                friend1 = friendship[0] -1
                friend2 = friendship[1] -1

                one_pair = False
                for lang in languages[friend1]:
                    if lang in languages[friend2]:
                        one_pair = True
                        break
                if i in languages[friend1]:
                    taughtIndividuals[friend1] = True
                if i in languages[friend2]:
                    taughtIndividuals[friend2] = True
                    
                if not one_pair:
                    if taughtIndividuals[friend1] and taughtIndividuals[friend2]:
                        continue
                    elif taughtIndividuals[friend1]:
                        taughtIndividuals[friend2] = True
                        taught +=1
                    elif taughtIndividuals[friend2]:
                        taughtIndividuals[friend1] = True
                        taught +=1
                    else:
                        taughtIndividuals[friend1] = True
                        taughtIndividuals[friend2] = True
                        taught +=2
            best = min(best,taught)
        return best


        # m = [0]*n
        # for group in groups:
        #     temp = [0]*n
        #     for individual in group:
        #         for lang in languages[individual]:
        #             temp[lang - 1] += 1
        #     print(temp, len(group))
        # return min(m)
