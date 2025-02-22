# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """

            1

        """

        levels = {}

        count = 0
        currItem = ""
        numNodes = 0

        i = 0
        while i < len(traversal):
            if traversal[i] == '-':
                count +=1
                i +=1
            else:
                numNodes += 1
                while i < len(traversal) and traversal[i] != '-':
                    currItem += traversal[i]
                    i +=1
                if count in levels:
                    levels[count].append((TreeNode(int(currItem),None,None),numNodes))
                else:
                    levels[count] = [(TreeNode(int(currItem),None,None),numNodes)]
                count = 0
                currItem = ""


        
        # print(levels)
        levelsPtr = [0]* len(levels)


        for level in levels:
            if level + 1 not in levels:
                break
            for index in range(len(levels[level])):

                currNode = levels[level][index][0]
                currIndex = levelsPtr[level]
                nextNodeIndex = float('inf')
                if index + 1 < len(levels[level]):
                    nextNodeIndex = levels[level][index + 1][1]

                print("currNode" ,currNode.val, "nextNode", nextNodeIndex)
                for i in range(currIndex,  currIndex + 2):
                    val = (i - currIndex )% 2
                    addedNode = None
                    if i < len(levels[level + 1]) and levels[level + 1][i][1] < nextNodeIndex: 
                        addedNode = levels[level + 1][i][0]
                        levelsPtr[level] += 1
                    
                    if val == 0:
                        currNode.left = addedNode
                    else:
                        currNode.right = addedNode

        if len(levels)== 0:return None
        return levels[0][0][0]
            
