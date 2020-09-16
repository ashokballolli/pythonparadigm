# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/188022
# Longest Substring Without Repeating Characters
# Input: s = "abcabcbb"
# Output: 3

class Solution:
    def lengthOfLongestSubstring01(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

    def lengthOfLongestSubstring02(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]

            str_list.append(x)
            max_length = max(max_length, len(str_list))

        return max_length

input_str = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring01(input_str))
print(sol.lengthOfLongestSubstring02(input_str))