def encript(Pin):
    Epin=" "
    for x in Pin:
        digit=int(x)
        num=(digit+5)%8
        Epin=Epin+str(num)
    return Epin

def decript(Epin):
    Dpin=" "
    for x in Epin:
        digit=int(x)
        if digit==6 or digit==7:
            Dpin=Dpin+str(digit-5)
        else:
            Dpin=Dpin+str(digit+3)
    return Dpin

userPin=input("Enter the Pin Number: ")
Encripted_Pin = encript(userPin)
print(Encripted_Pin)

userEpin=input("Enter the Encripted Pin Numbber: ")
Decripted_Pin = decript(userEpin)
print(Decripted_Pin)
