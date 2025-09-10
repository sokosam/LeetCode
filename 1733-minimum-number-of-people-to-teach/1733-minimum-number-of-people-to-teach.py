class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        langs = [set(lst) for lst in languages]

        # users who are in pairs that can't communicate
        bad_users = set()
        for a, b in friendships:
            a -= 1; b -= 1
            if langs[a].isdisjoint(langs[b]):
                bad_users.add(a)
                bad_users.add(b)

        # try teaching each language to just the needed bad_users
        best = float('inf')
        for L in range(1, n + 1):
            need = sum(1 for u in bad_users if L not in langs[u])
            best = min(best, need)
        return 0 if best == float('inf') else best
