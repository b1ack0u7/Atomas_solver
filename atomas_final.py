# -*- coding: utf-8 -*-
import os
from class_suma import suma_core

ini=[]
art=[]
dicc={}
ars={} 
debug={}

def fn_clear():
    if (os.name == 'nt'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def suma():
    art.clear()
    dicc.clear()
    for i in range(1,len(ini)+1):
        ini.insert(i,"+")
        art.append(ini.copy())
        ini.pop(i)
        
    for i in range(0,len(art)):
        dicc[i]=suma_core(art[i])


def det():
    tmp=[]
    for i in range(0,len(dicc)):
        tmp.append(len(dicc[i]))
        
    mn=min(tmp)
    for i in range(0,len(dicc)):
        if(len(dicc[i]) == mn):
            tmp.clear()
            tmp.append(dicc[i])
            tmp.append(art[i])
            ars[i]=tmp.copy()
            
    mn=min(ars)
    mx=max(ars)
    if (mn != mx):
        try:
            for i in range(mn,mx+1):
                print("Resultado: ",ars[i][0])
                print("Mejor opcion [%d]: "%i,ars[i][1],"\n")
        except:
            pass
    else:
        print("Resultado: ",ars[mn][0])
        print("Mejor opcion [%d]: "%mn,ars[mn][1],"\n")
    

def suma_main():
    global ini
    suma()
    det()
    try:
        y=int(input("Numero de array: "))
        if (y >= 0 and y <= len(dicc)):
            ini.clear()
            ini=dicc[y].copy()
            ars.clear()
            art.clear()
            dicc.clear()
            fn_clear()
        else:
            print("Se queda igual\n\n") 
    except:
        print("Se queda igual\n\n")


def resta():
    global ini
    ini_cpy=ini.copy()
    ini_cpy.sort()
    tmp=ini_cpy.copy()
    tmp=list(dict.fromkeys(tmp))
    
    var_sdp=[]
    var_ndp=[]
    
    for i in range(0,len(tmp)):
        msc=0
        for z in range(0,len(ini_cpy)):
            if (ini_cpy[z] == tmp[i]):
                msc=msc+1
        if(msc > 1):
            var_sdp.append(tmp[i])
        else:
            var_ndp.append(tmp[i])
    
    if (len(var_sdp) == len(tmp)):
        print("")
        print("[?] Eleccion del usuario")
        pausa=input("Enter para continuar\n")
        fn_clear()
    else:
        tmp.clear()
        tmp=ini_cpy.copy()
        mn=min(var_ndp)
        tmp.pop(tmp.index(mn))
        print("Se recomienda quitar el [%d]: "%mn,ini_cpy,"-->",tmp)
        x=str(input("Si / No: "))
        print("")
        
        if (x == "si" or x == "s" or x == "y"):
            ini.clear()
            ini=tmp.copy()
            return True
        else:
            return False
    

def add_data(r):
    try:
        fnd=ini.index(r)
        ini.insert(fnd, r)
    except:
        ini.append(r)


while True:
    try:
        print("")
        x=int(input("Datos iniciales: "))
        if(x<=0):
            break
        else:
            ini.append(x)
    except:
        break
fn_clear()

while True:
    print("Array actual -->",ini)
    try:
        print("")
        x=int(input("Ingrese su valor: "))
    except:
        print("")
        print("Adios")
        break
    if (x > 0):
        add_data(x)
        
    if (x == 0):
        fn_clear()
        suma_main()
        
    if (x < 0):
        op=resta()
        if (op == True):
            suma_main()