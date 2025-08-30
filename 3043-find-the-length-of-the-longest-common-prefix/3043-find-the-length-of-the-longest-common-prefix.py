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
                    return False
                else:
                    curr = self.start[i]
            elif i not in curr.next:
                return False
            else:
                curr = curr.next[i]
        return curr.end


        

    def startsWith(self, prefix: str) -> int:
        curr = None
        ans = 0
        for i in prefix:
            if curr == None:
                if i not in self.start:
                    return ans
                else:
                    curr = self.start[i]
                    ans +=1
            elif i not in curr.next:
                return ans
            else:
                curr = curr.next[i]
                ans += 1
        return ans



class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        

        arr1 = [str(i) for i in arr1]

        prefix = Trie()
        for i in arr1:
            prefix.insert(i)

        ans = 0

        for i in arr2:
            ans = max(ans, prefix.startsWith(str(i)))
        return ans