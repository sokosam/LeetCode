from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        adjacency_list = defaultdict(set)
        visited = set()

        for account in accounts:
            first_email = account[1]
            for j in range(2, len(account)):
                other_email = account[j]
                adjacency_list[first_email].add(other_email)
                adjacency_list[other_email].add(first_email)


        def dfs(account, emails):
            emails.add(account)
            visited.add(account)
            for adj in adjacency_list[account]:
                if adj in visited:
                    continue
                else:
                    dfs(adj, emails)
        
        ans = []

        for account in accounts:
            account_name = account[0]
            apart = set()

            if account[1] in visited:
                continue
            dfs(account[1], apart)

            ans.append([account_name] + sorted(list(apart)))
        return ans



