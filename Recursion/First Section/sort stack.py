def minAtBottom(stack, bottomPos):
    if len(stack) == bottomPos:
        return
    top = stack.pop()
    temp = stack[len(stack)-1]

    if temp > top:
        temp, top = top, temp
        stack[len(stack) - 1] = temp

    minAtBottom(stack, bottomPos)

    stack.append(top)
    return


def Sorted(s):
    if len(s) == 1:
        return
    stackSize = len(s)
    for i in range(1, stackSize+1):
        minAtBottom(s, i)

a = [5,1,3,4,2]
Sorted(a)