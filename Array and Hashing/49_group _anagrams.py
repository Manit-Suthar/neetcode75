from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defaultdict(list) automatically creates an empty [] if a key doesn't exist yet
        res = defaultdict(list)

        for word in strs:
            # Create a 26-zero array representing letters 'a' through 'z'
            count = [0] * 26

            for ch in word:
                # ord(ch) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
                count[ord(ch) - ord('a')] += 1

            # Convert the mutable list into an immutable tuple so it can be a dict key
            res[tuple(count)].append(word)

        # Return all the grouped lists stored as values in the dictionary
        return list(res.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))