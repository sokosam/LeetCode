# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        left = []
        center = []
        right = []

        q =deque()
        q.append([root, 0, 0])

        while q:
            curr = q.popleft()
            node = curr[0]
            level = curr[1]
            row = curr[2]

            if level == 0:
                while len(center) <= row:
                    center.append([])
                center[row].append(node.val)

            elif level < 0:
                if len(left) < abs(level):
                    left.append([])
                while len(left[abs(level) -1]) <= row:
                    left[abs(level) -1].append([])
                left[abs(level)  -1][row].append(node.val)
            else:
                if len(right) < abs(level):
                    right.append([])
                while len(right[abs(level) -1]) <= row:
                    right[abs(level) -1].append([])
                right[abs(level)  -1][row].append(node.val)
            

            if node.left:
                q.append([node.left, level - 1, row + 1])
            if node.right:
                q.append([node.right, level + 1, row + 1])
        left.reverse()

        for i in left:
            for j in i:
                j.sort()
        for i in right:
            for j in i:
                j.sort()
        for i in center:
            i.sort()
    
        ans = []
        for col in left:
            temp = []
            for row in col:
                for item in row:
                    temp.append(item)
            ans.append(temp)


        # for i in left:
        #     for j in left:
        #         temp = []
        #         for l in j:
        #             for item in l:
        #                 temp.append(item)
        #     ans.append(temp)
        
        temp = []
        for l in center:
            for item in l:
                temp.append(item)
        ans.append(temp)
        for col in right:
            temp = []
            for row in col:
                for item in row:
                    temp.append(item)
            ans.append(temp)

                    
        return ans
