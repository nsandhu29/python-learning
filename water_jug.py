def water_jug(a,b,c):
    if a%b == 0:
        return('We can\'t solve this problem' )
    water_left = 0
    temp1 = b
    temp2 = 0
    while water_left != c:
        #while temp2 != a:
        if b < (a-temp2):
            temp2 = b
            temp1 = 0
        water_left = temp2
        if temp2 !=a:
            temp2 = temp2 +(a - temp2)
            temp1 = 



