from qutip import *
ket0 = basis(2,0)
ket1 = basis(2,1)
X = sigmax()
Y = sigmay()
Z = sigmaz()
ket0 = basis(2,0) #! ket 0
ket1 = basis(2,1) #! ket 0
print("El ket 0  es:",ket0)
print("El ket 1  es:",ket1)
while True:
    preg =  int(input("""
    Escoge que multiplicación deseas ver:
    1.X y X
    2.Y y Y
    3.Z y Z
    4. X sobre ket0
    5. X sobre ket1
    6. Salir)"""))
    if preg == 1:
        print(f"La multiplicación de las matrices es:",X*X)
    elif preg == 2:
        print(f"Que pasa si multiplicamos las matrices Y y Y" )
        print(f"La multiplicación de las matrices es:",Y*Y)
    elif preg == 3:
        print(f"Que pasa si multiplicamos las matrices Z y Z" )
        print(f"La multiplicación de las matrices es:",Z*Z)
    elif preg == 4:
        print("X aplicado al ket0 es:")
        print(X*ket0)
    elif preg == 5:
        print("X aplicado al ket1 es:")
        print(X*ket1)
    elif preg == 6:
        break
    else:
        print("Opcion no valida, ingresa una operación correcta")
