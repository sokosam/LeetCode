class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:


        """

        [0:s:0, 4, 1, 0:e:7]
        


        """
        times = [0]*n

        s = []

        for log in logs:
            idn,typ,time = log.split(':')
            idn,time = int(idn), int(time)
            if typ == "start":
                if len(s) == 0:
                    total = 0
                s.append([idn, time, 'start'])
            else:
                # prev = s.pop()
                total = 0
                while s and s[-1][-1] == 'elapse':

                    x = s.pop()
                    total += x[1]
                    # total += s.pop()[-1][1]
                prev = s.pop()
                elapsed = time - prev[1] + 1 
                times[idn] += elapsed - total
                if len(s) != 0:
                    s.append([idn, elapsed, 'elapse'])
        return times



