from qutip import *
import numpy as np
import time
ket0 = basis(2,0)
ket1 = basis(2,1)
X = sigmax()
Y = sigmay()
Z = sigmax()
H = 1 / np.sqrt(2)* (ket0*ket0.dag() + ket0*ket1.dag() + ket1*ket0.dag() - ket1*ket1.dag() )
while True:
    print(f"Bienvenido a este programa, vamos a realizar operaciones cuanticas")
    time.sleep(1)
    print(f"La primera operación es el producto entre Pauli X y el ket0")
    time.sleep(1)
    print(f"La segunda operación es el producto entre Pauli X y el ket1")
    time.sleep(1)
    print(f"La Tercera operación es el producto entre Pauli Y y el ket0")
    time.sleep(1)
    print(f"La Cuarta operación es el producto entre Pauli Y y el ket1")
    time.sleep(1)
    print(f"La Quinta operación es el producto entre Pauli Z y el ket0")
    time.sleep(1)
    print(f"La Sexta operación es el producto entre Pauli Z y el ket1")
    time.sleep(1)
    print(f"La Septima operación es el producto entre Hadamard y el ket0")
    time.sleep(1)
    x = int(input("Cual es las operaciones te gustaria mirar?(Ingresa numeros del 1 al 6)"))
    if x == 1:
        print(f"El producto del ket0 con la Matriz Pauli X es:", X*ket0)
    elif x == 2:
        print(f"El producto del ket1 con la Matriz Pauli X es:", X*ket1)
    elif x == 3:
        print(f"El producto del ket0 con la Matriz Pauli Y es:", Y*ket0)
    elif x == 4:
        print(f"El producto del ket1 con la Matriz Pauli Y es:", Y*ket1)
    elif x == 5:

        print(f"El producto del ket0 con la Matriz Pauli Z es:", Z*ket0)
    elif x == 6:
        print(f"El producto del ket1 con la Matriz Pauli Z es:", Z*ket1)
    elif x == 7:
        print(f"La matriz Hadamard, viene dada por {H}")
    else:
        print("Has ingresado un numero incorrecto")
