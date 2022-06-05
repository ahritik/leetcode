'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    start = 0
    end = 0
    maxLength = 0
    unique = set()
    
    while end < len(s):
        if s[end] not in unique:
            unique.add(s[end])
            end += 1
            maxLength = max(maxLength, len(unique))
        else:
            unique.remove(s[start])
            start += 1
    return maxLength

print("Input: abcabcbb  Output:",lengthOfLongestSubstring("abcabcbb"))
print("Input: bbbbb  Output:",lengthOfLongestSubstring("bbbbb"))
print("Input: pwwkew  Output:",lengthOfLongestSubstring("pwwkew"))