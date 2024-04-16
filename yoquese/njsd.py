def uno_cero(num,exp):
    if num == 0:
        return 0
    else:
        if num%10 == 0:
            return 1*10**exp + uno_cero(num//10,exp+1)
        else:
            return num%10*10**exp + uno_cero(num//10,exp+1)