class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] != "#":
                i += 1
            else:
                length = int(s[j:i])
                res.append(s[i+1:i+1+length])
                j = i + length + 1
                i = j
        return res