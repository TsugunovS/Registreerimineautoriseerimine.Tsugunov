from random import * 
import string
def Registreerimine(l:list,p:list):
    nimi=input("Sisestage login: ")
    v=int(input("1-Ese koostan parooli\n2-Arvuti genireerib\n"))
    if v==1:
        pass
    else:
        salasona=Salasona(5)
        l.append(nimi)
        p.append(salasona)

    return l,p

def Salasona(k:int):
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def Autoriseerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi: ")
    salasona=input("Sisesta oma salasõna: ")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere tulemast!")
        else:
            print("Vale salasõna!")
    else:
        print("Nimi eiole")
    

    

