# -*- coding: utf-8 -*-
"""unique_morse

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12zP-9znMoc27zmEGM2V_vW3qQKPqPqVW
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)