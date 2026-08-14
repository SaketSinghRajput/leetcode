class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        j = 0
        def findcommonch(j, strs):
            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i + 1][j]:
                    return ""

            return strs[0][j]
        
        min_len = min(len(s) for s in strs)
        
        max_str = ""

        for j in range(min_len):
            ch = findcommonch(j, strs)

            if ch == "":
                return max_str

            max_str += ch

        return max_str



        