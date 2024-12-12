class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {char: 0 for char in s}
        for char in s:
            count[char] += 1
        
        result = []
        for char in order:
            if char in count:
                result.append(char * count[char])
                count[char] = 0
        
        for char in count:
            result.append(char * count[char])
        
        return ''.join(result)
