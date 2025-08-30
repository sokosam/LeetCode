class TrieNode:
    def __init__(self, val, end= False):
        self.val = val
        self.end = end
        self.next = {}

class Trie:

    def __init__(self):
        self.start = {}
        

    def insert(self, word: str) -> None:
        curr = None

        for i in word:
            if curr == None and i in self.start:
                curr =self.start[i]
            elif curr == None:
                self.start[i] = TrieNode(i)
                curr = self.start[i]
            elif i in  curr.next:
                curr = curr.next[i]
            else:
                curr.next[i] = TrieNode(i)
                curr = curr.next[i]
        curr.end = True


        
    def search(self, word: str) -> bool:
        curr = None
        for i in word:

            if curr == None:
                if i not in self.start:
                    print(word,i)
                    return False
                else:
                    curr = self.start[i]
            elif i not in curr.next:
                print(word,i)
                return False
            else:
                curr = curr.next[i]
        return curr.end


        

    def startsWith(self, prefix: str) -> bool:
        curr = None
        for i in prefix:
            if curr == None:
                if i not in self.start:
                    return False
                else:
                    curr = self.start[i]
            elif i not in curr.next:
                return False
            else:
                curr = curr.next[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)