# -*- coding: utf-8 -*-
"""Running_sum_of_1d

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xSM2VJPDdu-w92hAFsQLFixTrt9Vndcd
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=[]
        j=0
        for i in range(len(nums)):
            j=j+nums[i]
            k.append(j)
        return k