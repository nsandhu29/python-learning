git # def water_jug(a,b,c):
#     if a%b == 0:
#         return('We can\'t solve this problem' )
#     water_left = 0
#     temp1 = b
#     temp2 = 0
#     while water_left != c:
#         #while temp2 != a:
#         if b < (a-temp2):
#             temp2 = b
#             temp1 = 0
#         water_left = temp2
#         if temp2 !=a:
#             temp2 = temp2 +(a - temp2)
#             temp1 = 


# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

# Operations allowed:
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


def gcd(a,b):
    if a < b:
        return gcd(b,a)
    elif b == 0:
        return a
    else:
        return(gcd(b,(a%b)))

def water_jug(a,b,c):
    #print(a,b,c)
    if a%b == 0:
        return False
    if c == gcd(a,b) or c%gcd(a,b) == 0:
        return True



def main():
    a = int(input('Enter first jug capacity: '))
    b = int(input('Enter second jug capacity: '))
    c = int(input('Enter amount required: '))
    print(water_jug(a,b,c))
    

if __name__ == '__main__':
    main()
