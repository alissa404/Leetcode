class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # .Counter() create a dict for recording the result
        hist=collections.Counter(s)
        # hist.keys()   
        # hist.values()
        
        # for recursive output
        if not s     or min(hist.values())>=k:
            return len(s)
        
        for key in hist.keys():
            if hist[key]<k:
                bad_char=key

        substrings=s.split(bad_char)
        print(substrings)

        # recursive 
        sub_problems={self.longestSubstring(substring,k) for substring in substrings}
        # use dict or list  because later we use max()
        return max(sub_problems)