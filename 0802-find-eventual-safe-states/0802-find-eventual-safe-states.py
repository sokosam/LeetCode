class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """

        terminal nodes have out direction 0
        all nodes with a cycle are not apart of the return

        topological sort (khans algorithm) is O(V + E)
        if we were to run it for all V we have O(V*(V + E)) = O(V^2 + VE)

        indirection[4] = 0
        

        """


        ans = set()
        def dfs(adj, V, ans):
            seen = [False] * V
            rec_stack = [False] * V

            for i in range(V):
                if not seen[i] and is_cyc_util(adj, i, seen, rec_stack, ans):
                    ans.add(i)



                
        def is_cyc_util(adj, u, visited, rec_stack, ans):
        
            if not visited[u]:
            
                # Mark the current node as visited
                # and part of recursion stack
                visited[u] = True
                rec_stack[u] = True

                # Recur for all the vertices 
                # adjacent to this vertex
                for x in adj[u]:
                    if not visited[x] and is_cyc_util(adj, x, visited, rec_stack, ans):
                        ans.add(u)
                        return True
                    elif rec_stack[x]:
                        ans.add(u)
                        return True

            # Remove the vertex from recursion stack
            rec_stack[u] = False
            return False
        dfs(graph, len(graph), ans)
        # print(ans)
        ans = list(ans)
        ans = [i for i in range(len(graph)) if i not in ans]
        ans.sort()
        return ans