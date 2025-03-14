def rotateString(s, i):
    rotated = s[i:] + s[:i]
    return rotated

r = rotateString("abcdef", 2)
print(r)

def checkRotation(s):
    for i in range(len(s)):
        rotated = rotateString(s, i)
        if rotated == s:
            return True
    return False