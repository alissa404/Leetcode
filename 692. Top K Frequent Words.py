from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        # 先比「次數」(加負號 變降序)，次數一樣再比「單字字母」(升序)
        unique_words = sorted(count.keys(), key=lambda w: (-count[w], w))
        ans = []
        for i in range(k):
            # 取出排序後的前 k 個單字
            ans.append(unique_words[i])
        return ans