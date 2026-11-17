class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        our_keys = {}

        for string in strs:
            if "".join(sorted(string)) in our_keys:
                our_keys["".join(sorted(string))].append(string)
            else:
                our_keys["".join(sorted(string))] = [string]

        return [value for value in our_keys.values()]
 
            
