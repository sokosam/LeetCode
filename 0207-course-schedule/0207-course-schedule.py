class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for pre in prerequisites:
            if pre[0] not in courses:
                courses[pre[0]] = [pre[1]]
            else:
                courses[pre[0]].append(pre[1])
        
        works = set()
        def check(seen, course, works, courses):
            if course in works or course not in courses:
                return True
            if seen[course]:
                return False
            
            seen[course]= True
            ans = True
            for i in courses[course]:
                ans = ans and check(seen,i,works,courses)
            seen[course] = False
            return ans
        for i in range(numCourses):
            if i not in courses: continue
            seen = [False]* numCourses
            if check(seen,i,works,courses):
                works.add(i)
            else:
                return False

        return True
