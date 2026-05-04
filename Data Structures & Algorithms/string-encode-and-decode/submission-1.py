class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            n = str(len(s))
            enc += n + "₹" + s
        
        return enc



    def decode(self, s: str) -> List[str]:
        dec = []
        n = len(s)
        num = ""
        i = 0
        while i < n:
            if s[i] == "₹":
                length = int(num)
                dec.append(s[i + 1: i + length + 1])
                num = ""
                i = i + length + 1
                continue
            
            num += s[i]
            i += 1

        return dec
        
        
            

