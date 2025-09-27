


class Node:
    def __init__(self, val, next = None):
        self.val = val
        if next is None:
            self.next = []
        else:
            self.next = next
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        threeTuples = defaultdict(set)

        people = defaultdict(list)
        inp = [[username[i], timestamp[i], website[i]] for i in range(len(username))]
        inp.sort(key=lambda x : x[1])
        for i in range(len(username)):
            name = inp[i][0]
            time = inp[i][1]
            site = inp[i][2]
            # people[name].append(site)
            people[name].append(Node(site))

            for j in range(0,len(people[name]) -1):
                people[name][j].next.append(people[name][-1])

        for person in people:
            for i in range(0,len(people[person]) - 2):
                q = deque()
                q.append([people[person][i]])

                while q:
                    curr = q.popleft()
                    if len(curr) == 3:
                        threeTuples[(curr[0].val, curr[1].val,curr[2].val)].add(person)
                        continue
                    last = curr[-1]
                    for k in last.next:
                        # print(person, last.val, k.val)
                        q.append(curr + [k])

        # Handle the case where there are no 3-sequences
        if not threeTuples:
            return []

        best_pattern = ()
        max_count = 0

        # Sort the patterns to iterate in lexicographical order
        # This simplifies tie-breaking
        sorted_patterns = sorted(threeTuples.keys())

        for pattern in sorted_patterns:
            count = len(threeTuples[pattern])
            if count > max_count:
                max_count = count
                best_pattern = pattern
        return list(best_pattern)





        