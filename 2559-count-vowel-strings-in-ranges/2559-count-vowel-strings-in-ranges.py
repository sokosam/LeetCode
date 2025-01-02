class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        

        prefix = [0]
        vowels = {'a', 'e', 'i','o','u'}

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix.append(prefix[i] + 1)
            else:
                prefix.append(prefix[i])

        ans = []

        for query in queries:
            ans.append(prefix[query[1] + 1] - prefix[query[0]])
        return ans