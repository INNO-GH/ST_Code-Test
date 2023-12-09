class Solution(object):
    def isValid(self, s):
        stack = [] # This is much easier because of append, del ...
        for c in s: # Just put data immediately
           if c in '([{': # 'in' fuction
                stack.append(c) 
           else: # '\' connects through lines
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['): # stack[-1]=top
                    return False
                stack.pop() # Just use pop function
        return not stack

# Just push '([{' or simply compare top with next value
