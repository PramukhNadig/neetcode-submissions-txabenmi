class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        letters = set()
        for word in words:
            for letter in word:
                letters.add(letter)
        for word in range(1, len(words)):
            w1, w2 = words[word-1], words[word]
            check = min(len(w1), len(w2))
            if w1[:check] == w2[:check] and len(w1) > len(w2):
                return ''
            for i in range(check):
                if w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    break

        exp = set()
        res = []
        def dfs(x, vis):
            if x in exp:
                return True
            if x in vis:
                return False
            vis.add(x)
            for nei in graph[x]:
                if not dfs(nei, vis):
                    return False
            vis.remove(x)
            res.append(x)
            exp.add(x)
            return True
        
        for letter in sorted(letters, reverse=True):
            if letter not in exp:
                vis = set()
                if not dfs(letter, vis):
                    return ''

        return ''.join(reversed(res))