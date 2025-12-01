class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """


            n = 2

            for any k batteries that have life > 0

            1 2 3 4

            0 0 => 2 1

            2 1

            1 0 => 1 4

            0 3 => 3 3

            0 0 

            
            n = 2, batteries = [1,2,3,4]

            4 3

            4 5

            5 5
            
            n = 3, batteries = [1,2,3,4]

            4 3 2

            4 3 3

        """

        if len(batteries) == 1:
            if n > 1:
                return 0
            else:
                return batteries[0]
        if n == 1:
            return sum(batteries)
        if len(batteries) == n:
            return min(batteries)


        # m = defaultdict(int)

        # for i in batteries:
        #     m[i] +=1

        # unique = set(batteries)
        # unique = list(batteries)
        # unique.sort()

        bats = [-i for i in batteries]
        heapify(bats)

        m = defaultdict(int)
        seen = set()

        while n > 0:
            curr= heapq.heappop(bats)
            m[-curr] +=1
            seen.add(-curr)
            n -=1
        
        seen = list(seen)
        seen.sort()
        extra = -sum(bats)
        # print(seen, extra, bats)
        for i in range(len(seen) - 1):
            curr = seen[i]

            if m[curr] > extra:
                return curr
            next_num = seen[i + 1]
            count = m[curr]

            amount_needed = (next_num - curr)*count
            amount_possible = extra 

            if amount_needed > amount_possible:
                return amount_possible//count + curr
            else:
                m[next_num] += m[curr]
                extra -= amount_needed
                m[curr] = 0
        
        curr = seen[-1]
        return curr + extra//m[curr]





        




        # computer_heap = [0]*n
        # batteries = [-i for i in batteries]
        # heapq.heapify(batteries)

        # while len(batteries) > 1:
        #     curr_computer = heapq.heappop(computer_heap)

        #     curr_battery = -heapq.heappop(batteries)
        #     heapq.heappush(computer_heap,curr_computer + curr_battery)

        # curr_battery = -heapq.heappop(batteries)

        # while curr_battery > 0:
        #     curr_computer = heapq.heappop(computer_heap)
        #     heapq.heappush(computer_heap,curr_computer + 1)
        #     curr_battery -=1
        # print(computer_heap)
        # return min(computer_heap)



        # 5 5 5 (5, 5, 5, 5, 3)
        # 8 8 8 (2, 2, 2, 5, 3)
        # 10 10 10 (0,0,2,3,3)
        # 12 12 12 (2,2)
        # print(computer_heap)


        """
            10 10 6 9 3

 
        5 5 5     

        """

        # last_battery = curr_battery//n
        # mod_last = curr_battery % n
        # print(last_battery, mod_last, curr_battery)

        # curr_computer = heapq.heappop(computer_heap)
        # print(curr_computer)
        # heapq.heappush(computer_heap,curr_computer + mod_last)


        # max_min  = min(computer_heap) + last_battery

        # print(computer_heap)
        # return 0

