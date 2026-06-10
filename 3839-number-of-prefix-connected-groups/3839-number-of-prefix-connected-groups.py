class TrieNode:
    def __init__(self, val, hasPre):
        self.val = val
        self.hasPre = hasPre
        self.next = {}
class Trie:
    def __init__(self):
        self.total = 0
        self.tree = TrieNode(-1,-1)
    def add(self, word, k):
        curr = self.tree
        for index, char in enumerate(word):
            if char in curr.next:
                if index +1 == k and not curr.next[char].hasPre:
                    self.total +=1
                    curr.next[char].hasPre = True
            else:
                new_node = TrieNode(char,False)
                curr.next[char] = new_node
            curr = curr.next[char]
 



class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        trie = Trie()
        for word in words:
            trie.add(word,k)
        return trie.total
        