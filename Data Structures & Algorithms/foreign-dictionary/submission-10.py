class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        outgoing = {}
        graph = {}

        prev = None

        for w in words:

            # first word
            if not prev:
                prev = w
                for ch in w:
                    graph[ch] = set()
                continue

            # get first non same chr
            for i in range(len(w)):
                if i < len(prev):
                    if prev[i] != w[i]:
                        if w[i] not in graph:
                            graph[w[i]] = set()
                        graph[prev[i]].add(w[i])
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
                i += 1

            prev = w
        
        for ch in graph:
            outgoing[ch] = len(graph[ch])

        count = 0
        curr = []
        for ch in outgoing:
            if outgoing[ch] == 0:
                count += 1
                curr.append(ch)
        
        if count == 0:
            return ""


        result = ""

        # topological sort
        stack = []
        stack.extend(curr)

        print(stack)

        while stack:
            node = stack.pop()
            result += node

            for n in graph:
                if node in graph[n]:
                    outgoing[n] -= 1
                    if outgoing[n] == 0:
                        stack.append(n)

        for ch in graph:
            if outgoing[ch] != 0:
                return ""
            if ch not in result:
                result += ch
        return result[::-1]
            


