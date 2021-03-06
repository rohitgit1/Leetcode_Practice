# -*- coding: utf-8 -*-
"""Longest Palindromic Substring

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixGhog27v83jMAJQn1zNkmTGQlFvafaO
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r):
            while (l >= 0 and r < len(s) and s[l] ==s [r]):
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            test=helper(i,i)
            if len(test)>len(res):
                res = test
            test=helper(i,i+1)
            if len(test) > len(res):
                res = test
        return res