class Solution:
    def expand(self, s: str) -> List[str]:
        input_str = s
        r = 0
        size = len(input_str)
        collection = []
        curr_str = ""

        while r < size:
            if input_str[r] == "{":
                if len(curr_str ) > 0:
                    collection.append(curr_str)
                curr_str = ""
            elif input_str[r] == "}":
                collection.append(curr_str + "}")
                curr_str = ""
                r +=1
                continue
            curr_str += input_str[r]
            r+=1
            
        
        if len(curr_str) > 0:
            collection.append(curr_str)

        for index,i in enumerate(collection):
            if len(i) > 1 and i[0] == "{" and i[-1] == "}":
                collection[index] = i[1:len(i) - 1]
                collection[index] = collection[index].split(',')
            else:
                collection[index] = [collection[index]]
            

        all_expanded_strings = []
        def backtracking(collection, i, current):
            nonlocal all_expanded_strings
            if i >= len(collection):
                all_expanded_strings.append("".join(current))
                return
            
            for candidate in collection[i]:
                current.append(candidate)
                backtracking(collection, i + 1, current)
                current.pop()
        backtracking(collection, 0, [])

        all_expanded_strings.sort()
        return all_expanded_strings