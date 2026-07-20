# Given a string containing just the characters '(' and ')',
# return the length of the longest valid (well-formed) parentheses substring.
def longestValidParentheses(s):
    stack = [-1]  # Initialize stack with -1
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# Example usage:
s = "(()())"    
print(longestValidParentheses(s))  # Output: 6