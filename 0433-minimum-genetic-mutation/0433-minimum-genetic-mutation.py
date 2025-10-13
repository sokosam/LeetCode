class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene != endGene and endGene not in bank:
            return -1

        m = defaultdict(set)
        for gene in bank:
            for i in range(len(gene)):
                val = gene[0:i] + "*" + gene[i + 1:]
                m[val].add(gene)
        
        seen = set()


        q =deque()

        q.append([startGene,0])
        seen.add(startGene)

        while q:
            gene, count  = q.popleft()
            if gene == endGene:
                return count
            for i in range(len(gene)):
                val = gene[0:i] + "*" + gene[i + 1:]
                for i in m[val]:
                    if i not in seen:
                        seen.add(i)
                        q.append([i, count + 1])
        return -1

