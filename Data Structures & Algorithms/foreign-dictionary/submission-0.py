class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        incoming = {}
        outgoing = {}
        graph = {}

        prev = None

        for w in words:

            # first word
            if not prev:
                prev = w
                for ch in w:
                    graph[ch] = set()
                    incoming[ch] = 0
                    outgoing[ch] = 0
                continue

            # get first non same chr
            for i in range(len(w)):
                if i < len(prev):
                    if prev[i] != w[i]:
                        if w[i] not in graph:
                            graph[w[i]] = set()
                        if w[i] not in incoming:
                            incoming[w[i]] = 0
                        if w[i] not in outgoing:
                            outgoing[w[i]] = 0
                        incoming[w[i]] += 1
                        # add outgoing
                        graph[w[i]].add(prev[i])
                        outgoing[prev[i]] += 1
                        break
                else:
                    break

            # add remaining chrs to graph
            while i < len(w):
                if w[i] not in graph:
                    graph[w[i]] = set()
                if w[i] not in incoming:
                    incoming[w[i]] = 0
                if w[i] not in outgoing:
                    outgoing[w[i]] = 0
                i += 1

            prev = w
        
        count = 0
        for ch in incoming:
            if incoming[ch] == 0:
                if count == 0:
                    count += 1
                else:
                    # invalid
                    return ""
        
        # invalid
        if count == 0:
            return ""

        count = 0
        curr = None
        for ch in outgoing:
            if outgoing[ch] == 0:
                if count == 0:
                    count += 1
                    curr = ch
                else:
                    return ""
        
        if count == 0:
            return ""


        result = ""

        # topological sort
        stack = [curr]
        visited = set()
        visited.add(curr)

        while stack:
            node = stack.pop()
            result += node

            for n in graph[node]:
                if n in visited:
                    return ""
                
                visited.add(n)
                outgoing[n] -= 1
                if outgoing[n] == 0:
                    stack.append(n)

        return result[::-1]
            


