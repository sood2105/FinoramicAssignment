class Solution:
# @param A : string
# @return an integer
    def braces(self, A):
        stack=[]
        # flag=True
        for i in A:
            if (i==')'):
                top_element=stack.pop()
                flag=True
                while (top_element != '('):
                    if (top_element=='+' or top_element=='-' or top_element=='*' or top_element=='/'):
                        flag=False
                    top_element=stack.pop()
                if (flag==True):
                    return 1
            else:
                stack.append(i)
        return 0