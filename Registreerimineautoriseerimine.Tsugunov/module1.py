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

def MuudaParool(vana_p, uus_p:float):
    valik = int(input("1 - muuda login; 2 - muuda parool: "))
    
    if valik == 1:
        uus_nimi = input("Sisestage uus login: ")
        print("Login muudetud")
        return uus_nimi
    elif valik == 2:
        if vana_p == input("Sisestage vana parool: "):
            uus_p = input("Sisestage uus parool: ")
            print("Parool muudetud")
            return uus_p
        else:
            print("Vale parool!")
    else:
        print("Vigane valik")
    


    

    

