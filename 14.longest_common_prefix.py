class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        result = min(strs)
        temp = max(strs)
        for i, c in enumerate(result):
            # i 表示index
            # c 表示英文字母
            if c != temp[i]:
                return result[:i]
        return result
    
'''
如果不能用indexOf的話你會怎麼做？」
(可使用String.toCharArray()轉成陣列後再操作)
「如果這組陣列被預期長短差異很大呢？」
(先掃過一遍陣列，拿最短的當pre)
「Best Case和Worst Case的時間複雜度？什麼狀況下會發生？」
(依照你的解法應該有所不同)
「如果加入<0的判斷式的話可以提升這個程式的效率嗎？」
(不一定，因為不保證多快能遇到前綴完全不同的字串，
所以端看這組資料是預期很有可能出現結果為空字串，
還是大多數都會有共同前綴來決定。)
'''