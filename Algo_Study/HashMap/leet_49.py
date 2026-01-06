from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = {}

        for s in strs:
            sorted_s = "".join(sorted(s)) # 정렬해서 딕셔너리에 append

            if sorted_s not in dic:
                dic[sorted_s] = [s]
            else:
                dic[sorted_s].append(s)

        for key in dic:
            result.append(dic[key])

        return result

print(Solution.groupAnagrams(Solution(), ["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams(Solution(), [""]))
print(Solution.groupAnagrams(Solution(), ["a"]))