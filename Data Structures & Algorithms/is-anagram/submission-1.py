class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1.keys():
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in dict1.keys():
                return False
            else:
                if t[j] not in dict2.keys():
                    dict2[t[j]] = 1
                else:
                    dict2[t[j]] += 1

        for key, value in dict1.items():
            if dict1[key] != dict2[key]:
                return False

        return True
        


