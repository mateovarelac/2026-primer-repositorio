Encriptado=""
abecedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Cod_dividido=[]
Cod_desdividido=[]
print("--------------------------------------------- \n Bienvenido! Esto es un encriptador Cesar \n --------------------------------------------")
A_encriptar=input("Introduzca el código a encriptar: ")
while True:
    Num_encriptar=input("Introduzca cuantos espacios quiere mover su número \n Rta: ")
    if Num_encriptar.isdigit():
        Num_encriptar=int(Num_encriptar)
        if Num_encriptar>27:
            while Num_encriptar>27:
                Num_encriptar-=27
        break
    else:
        print("Valor no válido, por favor introduzca un número")
for a in A_encriptar:
    Cod_dividido.append(a.lower())
for a in range(len(Cod_dividido)):
    if abecedario.index(Cod_dividido[a])+Num_encriptar>26:
        Cod_dividido[a]=abecedario[abecedario.index(Cod_dividido[a])+Num_encriptar-27]
    else:
        Cod_dividido[a]=abecedario[abecedario.index(Cod_dividido[a])+Num_encriptar]

print(Cod_dividido)

print("Ahora procederemos a descodificar el código.")
while True:
    Num_encriptar=input("Introduzca cuantos espacios se movió su palabra original \n Rta: ")
    if Num_encriptar.isdigit():
        Num_encriptar=int(Num_encriptar)
        if Num_encriptar>27:
            while Num_encriptar>27:
                Num_encriptar-=27
        break
    else:
        print("Valor no válido, por favor introduzca un número")
for a in range(len(Cod_dividido)):
    if abecedario.index(Cod_dividido[a])-Num_encriptar<0:
        Cod_desdividido.append(abecedario[abecedario.index(Cod_dividido[a])-Num_encriptar+27])
    else:
        Cod_desdividido.append(abecedario[abecedario.index(Cod_dividido[a])-Num_encriptar])
print(Cod_desdividido)