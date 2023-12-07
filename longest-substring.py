def lengthOfLongestSubstring(s: str) -> int:
    # n = len(s)
    # charSet = set()
    # maxLength = 0
    # left = 0
    # for right in range(n):
    #     if s[right] not in charSet:
    #         charSet.add(s[right])
    #         maxLength = max(maxLength, right - left + 1)
    #     else:
    #         while s[right] in charSet:
    #             charSet.remove(s[left])
    #             left += 1
    #         charSet.add(s[right])
    # return maxLength

    n = len(s)
    maxLength = 0
    charIndex = [-1] * 128
    left = 0
    
    for right in range(n):
        if charIndex[ord(s[right])] >= left:
            left = charIndex[ord(s[right])] + 1
        charIndex[ord(s[right])] = right
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))