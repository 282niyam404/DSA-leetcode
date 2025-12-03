class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []

        char_count = Counter(chars)

        for w in words:
            w_count = Counter(w)
            if all(w_count[c] <= char_count[c] for c in w_count):
                res.append(len(w))

        return sum(res)
        