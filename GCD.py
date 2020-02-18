def gcd(a,b):
    if a < b:
        return gcd(b,a)
    elif b == 0:
        return a
    else:
        return(gcd(b,(a%b)))

def main():
    a = int(input('Please enter first number: '))
    b = int(input('Please enter first number: '))
    result = gcd(a,b)
    print('gcd(%d,%d) = %d'% (a,b,result))

if __name__ == '__main__':
    main()
    