def MoveTopToPos(St, pos):
    if len(St) == pos:
        return
    top = St.pop()
    temp = St[len(St)-1]
    top, temp = temp, top
    St[len(St)-1] = temp
    MoveTopToPos(St, pos) 
    St.append(top)
    return   

def reverse1(St):
    size = len(St)
    if size == 1:
        return
    for i in range(1, size+1):
        MoveTopToPos(St,i)

    return

def moveElementToBottom(St, elem):
    if len(St) != 0:
        top = St.pop()
        moveElementToBottom(St, elem)
        St.append(top)
    else:
        St.append(elem)

def reverse2(St):
    if len(St) == 0:
        return
    top = St.pop()
    reverse2(St)
    moveElementToBottom(St, top)





a = [5,1,3,4,2]
# reverse(a)
reverse2(a)
print(a)