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


def MuudaParool(l:list,p:list):
    nimi=input("Sisesta oma nimi: ") # запрос на имя пользователя
    salasona_vana=input("Sisesta oma vana salasõna: ")
    if nimi in l: # проверка пользователя
        ind=l.index(nimi) # нахождения пользователя в списке (nimi)
        if salasona_vana==p[ind]:
            salasona_uus = input("Sisesta oma uus salasõna: ")
            p[ind] = salasona_uus
            print("Salasõna muudetud!")
        else:
            print("Vale salasõna!")
    else:
        print("Nimi ei ole registreeritud.")

    return l, p

def MuudaLogin(l:list,p:list):
    vana_nimi = input("Sisesta oma vana nimi: ")
    if vana_nimi in l:
        uus_nimi = input("Sisesta oma uus nimi: ")
        ind = l.index(vana_nimi)
        l[ind] = uus_nimi
        print("Nimi muudetud")
    else:
        print("Nimi ei ole registreeritud.")

    return l, p

        

    

    

