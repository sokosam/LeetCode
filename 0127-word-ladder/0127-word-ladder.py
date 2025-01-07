from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Preprocessing to create adjacency list using patterns
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        # BFS Initialization
        queue = deque([(beginWord, 1)])  # (current_word, level)
        visited = set()
        visited.add(beginWord)

        while queue:
            curr_word, level = queue.popleft()

            # Check all neighbors by pattern matching
            for i in range(len(curr_word)):
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                for neighbor in adj[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                # Remove pattern to save memory
                adj[pattern] = []

        return 0
