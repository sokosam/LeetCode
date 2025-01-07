class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        def intervalSearch(newInterval, intervals, pos):
            if len(intervals) == 1:
                return 0 if intervals[0][pos] > newInterval[pos] else 1
            l = 0
            r = len(intervals) -1
            
            while l <= r:
                m = l + (r-l)//2
                if m != len(intervals) - 1 and intervals[m][pos] <= newInterval[pos] <= intervals[m +1][pos]:
                    return m + 1
                    
                elif m == len(intervals):
                    if intervals[m][pos] < newInterval[pos]:
                        return m + 1
                    else:
                        return m
                elif intervals[m][pos] < newInterval[pos]:
                    l = m + 1
                else:
                    r = m - 1
            if r < 0:
                return 0
            else:
                return len(intervals) 
        
        left = intervalSearch(newInterval, intervals, 0)
        right = intervalSearch(newInterval,intervals,1)
        ans = []

        for i in range(len(intervals)):
            if left <= i < right:
                continue
            ans.append(intervals[i])




        ans.insert(left, newInterval)
        deleteLeft = False
        if left != 0 and ans[left - 1][1] >= ans[left][0]:
            ans[left][0] = ans[left - 1][0]
            if ans[left- 1][1] > ans[left][1]:
                ans[left][1] = ans[left -1][1]
            deleteLeft = True
        if left != len(ans) - 1 and ans[left + 1][0] <= ans[left][1]:
            if ans[left + 1][1] > ans[left][1]:
                ans[left][1] = ans[left +1][1]
            del ans[left + 1]
        if deleteLeft: del ans[left -1]
            

        return ans