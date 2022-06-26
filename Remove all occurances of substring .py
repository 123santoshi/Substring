#leetocde link:-- https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

'''example:-
      Input: s = "daabcbaabcbc", part = "abc"
      Output: "dab"
      Explanation: The following operations are done:
      - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
      - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
      - s = "dababc", remove "abc" starting at index 3, so s = "dab".
      Now s has no occurrences of "abc".'''

class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        stack=[]
        l=len(part)
        for i in s:
            stack.append(i)
            if(len(stack)>=l):
                if("".join(stack[-l:])==part):
                    for j in range(l):
                        stack.pop()
        return "".join(stack)
