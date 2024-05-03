def longestValidParentheses(s):
    stack = []
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            stack.append(i+1)
        else:
            if len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i+1)

    stack.append(len(s))
    stack = [0]+stack
    mx = 0
    print(stack)
    for i in range(1, len(stack)):
        mx = max(mx, stack[i] - stack[i - 1])

    print(mx)


longestValidParentheses("(()")
longestValidParentheses(")()())")
