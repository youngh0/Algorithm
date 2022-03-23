from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()

        for letter in s:
            if letter.isalnum():
                strs.append(letter.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

