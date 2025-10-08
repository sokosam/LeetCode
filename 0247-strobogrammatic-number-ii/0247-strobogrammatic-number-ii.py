class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """
        the number has to be palindromic, in the case of 6/9 it can be either but mirrored on the otherside (by mirror we mean use the other)

        1 2 3 4 5 6 7 8 9 0

        1 0 8

        6 9

        for n >= 2 

        69 6x9 6xx9 x69x

        """
        available = [1,0,8,6]
        ans = []
        curr = [-1]*n
        def recurse(l,r):
            nonlocal curr
            if l > r:
                ans.append("".join(curr.copy()))
                return
            
            else:
                for num in available:
                    if num != 6:
                        if num == 0 and l == 0 and l != r:
                            continue
                        curr[l] = str(num)
                        curr[r] = str(num)
                        recurse(l + 1, r -1)
                    else:
                        if l == r:
                            continue
                        curr[l] = "6"
                        curr[r] = "9"
                        recurse(l + 1, r - 1)
                        curr[l] = "9"
                        curr[r] = "6"
                        recurse(l + 1, r- 1)
        recurse(0, n- 1)
        return ans