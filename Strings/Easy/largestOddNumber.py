def largestOddNUmber(num):
    pos = len(num)
    for i in range(len(num)-1,-1,-1):
        if int(num[i]) % 2 == 1:
            pos = i
            break
        else:
            pos = -1

    if pos == -1:
        return ""
    else:
        return num[:pos+1]
    
# Cleaner solution
def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[: i+1]
        return ''
    
print(largestOddNUmber("527"))