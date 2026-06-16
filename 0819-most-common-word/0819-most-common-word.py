class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-z]+", paragraph.lower())

        banned = set(banned)

        freq = Counter(word for word in words if word not in banned)

        return max(freq, key=freq.get)
        