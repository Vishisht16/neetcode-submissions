class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        s = "".join(strs)
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            # begin length loop
            length = 0
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                else:
                    length *= 10
                    length += int(s[i])
                    i += 1

            # begin slice word out of s
            word = s[i+1 : i+1+length]

            strs.append(word)
            i += length + 1
        
        return strs



