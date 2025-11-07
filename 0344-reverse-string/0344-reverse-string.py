# class Stack:
#     def __init__(self):
#         self.stack_list = []
class Solution(object):
    def reverseString(self, s):
        list = []
        for char in s:
            list.append(char)

     
        for i in range(len(s)):
            s[i] = list.pop()


        