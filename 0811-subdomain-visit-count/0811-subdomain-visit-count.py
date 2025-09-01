class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        

        m = defaultdict(int)

        for domain in cpdomains:
            vals = split(" ", domain)

            visits = int(vals[0])
            dom = vals[1]
            m[dom] += visits

            dom = dom.split('.')
            for i in range(len(dom)):
                m[".".join(dom[i +1:])] += visits

        print(m)
        
        ans = [str(m[key]) + " " + key for key in m if len(key) > 0]
        return ans






