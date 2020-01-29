def upperLower(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    
    return "No of Upper case Characters: "+str(upper)+"\nNo of Lower case Characters: "+str(lower)

print(upperLower("The Quick Brown Fox"))


def Max_Number(num1, num2, num3):
    numlist = [num1, num2, num3]
    maxnum = max(numlist)
    return maxnum

print(Max_Number(2,3,40))

def isPrime(num):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                return False
        return True
    else:
        return False

print(isPrime(40))
            