class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity) != complexity[0]:
            return 0

        m = Counter(complexity)
        if m[complexity[0]] > 1:
            return 0
        def fact(x):
            if x == 0 or x ==1:
                return 1
            return x*fact(x-1)
        ans = fact(len(complexity) - 1)
        for i in m :
            if m[i] > 1:
                ans//fact(m[i])



        return ans % (10**9 + 7)
