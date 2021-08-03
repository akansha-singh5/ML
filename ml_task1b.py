str1=input("Enter string:")
n=int(input("Enter integer:"))

for i in range(len(str1)):
    x=str1[i]
    a=ord(x)
    if(97<=a<=123):
        b=a+n
        if(b<=122):
            new=chr(b)
            print(new)
        else:
            b=96+b-122
            new=chr(b)
            print(new)
    else:
        pass
    

    
