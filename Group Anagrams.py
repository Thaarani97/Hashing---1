# TC : O(n*m^2 logm) # mlogm for sorting, m for finding the hashcode of the string. n is the length of the list
# SC : O(1) 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        
        res = []
        for k in anagrams:
            res.append(anagrams[k])
        
        return res