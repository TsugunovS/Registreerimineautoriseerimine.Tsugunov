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


def MuudaParool(l, p):
    """Toimingu valimise taotlus Запрос на выбор действия
    """
    valik = int(input("1 - muuda login; 2 - muuda parool: "))
    
    if valik == 1:
        #Uue kasutajanime taotlemine Запрос на новое имя пользоваттеля
        l=input("Sisestage vana ")
        uus_l= input("Sisestage uus login: ")
        print("Login muudetud")
        l.append(uus_l)
        return l==uus_l
    elif valik == 2:
        # Проверка правилбности введенного старого пароля
        if p == input("Sisestage vana parool: "):
            # Запрос на новый пароль
            uus_p = input("Sisestage uus parool: ")
            print("Parool muudetud")
            print(p==uus_p)
            return p==uus_p
        else:
            # сообщения об ошибке если неправильно веден старый пароль
            print("Vale parool!")
    else:
        # сообщения об ошибке если неправильно выбпано действие
        print("Vigane valik")

        

    

    

