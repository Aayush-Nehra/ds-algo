def removeOuterParenthesis(s):
    stack = list()
    ans = ""
    for i in range(len(s)):
        if len(stack) == 0  and s[i] == "(":
            stack.append("(")
        elif len(stack) != 0 and s[i] == "(":
            stack.append("(")
            ans += "("
        elif len(stack) != 1 and s[i] == ")":
            stack.pop()
            ans += ")"
        elif len(stack) == 1 and s[i] == ")":
            stack.pop()

    return ans

def removeOuterParenthesis2(s):
    leftParenthesisCount = 0
    ans = ""
    for i in range(len(s)):
        if leftParenthesisCount == 0  and s[i] == "(":
            leftParenthesisCount += 1
        elif leftParenthesisCount != 0 and s[i] == "(":
            leftParenthesisCount += 1
            ans += "("
        elif leftParenthesisCount != 1 and s[i] == ")":
            leftParenthesisCount -= 1
            ans += ")"
        elif leftParenthesisCount == 1 and s[i] == ")":
            leftParenthesisCount -= 1

    return ans

print(removeOuterParenthesis2("(()())(())"))