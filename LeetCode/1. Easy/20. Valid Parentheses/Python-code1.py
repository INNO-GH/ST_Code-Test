class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # I'll solve this by stack
        stack = ''
        for i in range(0, len(s)):
            stack=stack+s[i]   # Cannot use append in string, but use just +!
            if(len(stack)==1):
                continue
            top=stack[len(stack)-1]
            undertop=stack[len(stack)-2]
            if((undertop=='(' and top==')') or (undertop=='{' and top=='}') or (undertop=='[' and top==']') ):
                stack=stack.replace(undertop+top,'') # Cannot use del in string, but use replace fuction
        if(len(stack)==0): return True
        else: return False
