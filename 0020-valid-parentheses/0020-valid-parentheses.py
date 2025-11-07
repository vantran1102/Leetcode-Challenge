
class Solution(object):
    def isValid(self, s):
        my_list = []
        for c in s:
            if c in "([{":
                my_list.append(c)
            else:
                if not my_list:
                    return False
                if c == ")":
                    if my_list.pop()!="(":
                        return False
                elif c == ']':
                    if my_list.pop()!="[":
                        return False
                else:
                    if my_list.pop()!="{":
                        return False
        return not my_list
        