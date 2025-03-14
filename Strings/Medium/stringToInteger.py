def removeTrailingZeroes(str):
    lastTrailingZeroPos = 0
    for i in range(0, len(str)):
        if str[i] == "0":
            lastTrailingZeroPos += 1
        else:
            break
    return str[lastTrailingZeroPos:]

def getNumbersBeforeFirstNonNum(str):
    validStrLen = 0
    for i in range(0, len(str)):
        if str[i].isdigit():
            validStrLen += 1
        else:
            break
    return str[0:validStrLen]


def myAtoi(s):
    minNum = -pow(2,31)
    maxNum = pow(2,31) - 1
    #Trim Spaces
    trimmedString = s.strip()
    if trimmedString=="+" or trimmedString=="-" or trimmedString=="":
        return 0
    #Remove and Remember Sign
    isNegaitve = False
    skipSignChar = 0
    if trimmedString[0] == "-":
        isNegaitve = True
        skipSignChar = 1
    elif trimmedString[0] == "+":
        skipSignChar = 1

    stringWithoutSign = trimmedString[skipSignChar:]
    if not stringWithoutSign[0].isdigit():
        return 0
    stringWithoutZeroes = removeTrailingZeroes(stringWithoutSign)
    #Get Valid String
    validString = getNumbersBeforeFirstNonNum(stringWithoutZeroes)
    try:
        ans = int(validString)
    except:
        if stringWithoutSign[0] == "0":
            return 0

    if isNegaitve == True:
        ans = -ans

    if ans > maxNum:
        return maxNum
    elif ans < minNum:
        return minNum
    else:
        return ans

# print(myAtoi("-"))
# print(myAtoi("words and 987"))
# print(myAtoi("0-1"))
print(myAtoi("21474836460"))
# print(myAtoi("-"))
# print(myAtoi("-"))

# good solution
# while i < n and s[i].isdigit():
#     digit = int(s[i])
#     # Check for overflow
#     if result > (INT_MAX - digit) // 10:
#         return INT_MAX if sign == 1 else INT_MIN
#     result = result * 10 + digit
#     i += 1