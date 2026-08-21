class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # incoming = {}
        outgoing = {}
        graph = {}

        prev = None

        for w in words:

            # first word
            if not prev:
                prev = w
                for ch in w:
                    graph[ch] = set()
                    # incoming[ch] = 0
                    # outgoing[ch] = 0
                continue

            # get first non same chr
            for i in range(len(w)):
                if i < len(prev):
                    if prev[i] != w[i]:
                        if w[i] not in graph:
                            graph[w[i]] = set()
                        # if w[i] not in incoming:
                        #     incoming[w[i]] = 0
                        # if w[i] not in outgoing:
                        #     outgoing[w[i]] = 0
                        # incoming[w[i]] += 1
                        # add outgoing (i.e. prev is less than w)
                        graph[prev[i]].add(w[i])
                        # outgoing[prev[i]] += 1
                        break
                else:
                    break
            else:
                if prev != w:
                # prev is prefix but more length
                    return ""

            # add remaining chrs to graph
            while i < len(w):
                if w[i] not in graph:
                    graph[w[i]] = set()
                # if w[i] not in incoming:
                #     incoming[w[i]] = 0
                # if w[i] not in outgoing:
                #     outgoing[w[i]] = 0
                i += 1

            prev = w
        
        for ch in graph:
            outgoing[ch] = len(graph[ch])

        print(graph)
        print(outgoing)

        # count = 0
        # for ch in incoming:
        #     if incoming[ch] == 0:
        #         if count == 0:
        #             count += 1
        #         # else:
        #         #     # invalid
        #         #     return ""
        
        # # invalid
        # if count == 0:
        #     return ""

        count = 0
        curr = []
        for ch in outgoing:
            if outgoing[ch] == 0:
                count += 1
                curr.append(ch)
                # else:
                #     return ""
        
        if count == 0:
            return ""


        result = ""

        # topological sort
        stack = []
        stack.extend(curr)
        visited = set()
        for c in curr:
            visited.add(c)

        print(stack)

        while stack:
            node = stack.pop()
            result += node

            for n in graph:
                if node in graph[n]:
                    if n in visited:
                        continue
                    
                    visited.add(n)
                    outgoing[n] -= 1
                    if outgoing[n] == 0:
                        stack.append(n)
            print(stack)

        print(result)
        for ch in graph:
            if ch not in result:
                result += ch
        return result[::-1]
            


