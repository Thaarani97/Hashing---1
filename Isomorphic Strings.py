# Approach - 1
# TC: O(n)
# SC: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        for i in range(len(s)):
            if s[i] not in maps:
                if t[i] not in maps.values():
                    maps[s[i]] = t[i]
                else:
                    return False
            else:
                if t[i] != maps[s[i]]:
                    return False
                
        return True

# Approach - 2
# TC: O(n)
# SC: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
            else:
                if t[i] != maps[s[i]]:
                    return False
                
            if t[i] not in mapt:
                mapt[t[i]] = s[i]
            else:
                if s[i] != mapt[t[i]]:
                    return False
            
        return True