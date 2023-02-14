from module1 import * 
l=["Python"]
p=["12345"]

while True:
    print(l)
    print(p)
    v=int(input("1-Registreerimine\n2-Autoriseerimine\n3-Välja "))
    if v==1:
        Registreerimine(l,p)
        pass
    elif v=="":
        print("Autoriseerimine")
    elif v==2:
        Autoriseerimine(l,p)
    elif v==3:
        break
    else:
        print("Tee õige valik")


        