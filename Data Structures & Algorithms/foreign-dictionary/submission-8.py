class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        letters = set()
        for word in words:
            for letter in word:
                letters.add(letter)
        for i in range(1, len(words)):
            minLen = min(len(words[i]), len(words[i-1]))
            if (len(words[i-1]) > len(words[i])) and (words[i][:minLen] == words[i-1][:minLen]):
                return ''
            first, second = words[i-1], words[i]
            for j in range(minLen):
                if first[j] != second[j]:
                    graph[first[j]].add(second[j])
                    break
        vis = set()
        cycle = set()
        res = []
        def toposort(x):
            if x in vis:
                return True
            if x in cycle:
                return False
            cycle.add(x)
            for nei in graph[x]:
                if not toposort(nei):
                    return False
            res.append(x)
            vis.add(x)
            cycle.remove(x)
            return True
        for letter in letters:
            if not toposort(letter):
                return ''
        return ''.join(reversed(res))
        