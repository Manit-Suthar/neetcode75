class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 = dict()
        dict2 = dict()
        for ch in s:
            if ch not in dict1:
                dict1[ch] = 1
            else :
                dict1[ch] = dict1.get(ch)+1

            # char_count[char] = char_count.get(char, 0) + 1 checks if a character is already in the dictionary, retrieves its current count (or defaults to 0 if it's new), adds 1, and saves the updated total.
        for ch in t:
            if ch not in dict2:
                dict2[ch] = 1
            else:
                dict2[ch] = dict2.get(ch)+1
        
        return dict1 == dict2
    
print(Solution().isAnagram('anagram','nagarap'))