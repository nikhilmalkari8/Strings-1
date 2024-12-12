"Time Complexity is O(N)"
"Space Complexity is O(1)"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        start = 0
        longest = 0
        
        for i in range(len(s)):
            if s[i] in my_dict and my_dict[s[i]] >= start:
                start = my_dict[s[i]] + 1
            my_dict[s[i]] = i
            longest = max(longest, i - start + 1)
        
        return longest
        