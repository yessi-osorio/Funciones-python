from tkinter import ttk
from tkinter import *

window = Tk()

window.title("Examen Final")
window.geometry('500x300')

numero0 = Label(window, text="Bienvenido:", font=("Arial Bold", 20)).grid(row=1, column=1, columnspan=5)
#Creación de los labels
numero1 = Label(window, text="Nùmero 1:", font=("Arial Bold", 15)).grid(column=2, row=2)
numero2 = Label(window, text="Nùmero 2:", font=("Arial Bold", 15)).grid(column=2, row=3)
numero3 = Label(window, text="Nùmero 3:", font=("Arial Bold", 15)).grid(column=2, row=4)
numero4 = Label(window, text="Nùmero 4:", font=("Arial Bold", 15)).grid(column=2, row=5)
numero5 = Label(window, text="Nùmero 5:", font=("Arial Bold", 15)).grid(column=2, row=6)

#Entrada de datos
numero11 = Entry(window,width=30)
numero11.grid(column=4, row=2)

numero22 = Entry(window,width=30)
numero22.grid(column=4, row=3)

numero33 = Entry(window,width=30)
numero33.grid(column=4, row=4)

numero44 = Entry(window,width=30)
numero44.grid(column=4, row=5)

numero55 = Entry(window,width=30)
numero55.grid(column=4, row=6)



#Funciones de la aplicación

#Funcion 1: ordenar los números
def ordenar():
    a = int(numero11.get())
    b = int(numero22.get())
    c = int(numero33.get())
    d = int(numero44.get())
    e = int(numero55.get())
    
    lista=(a, b, c, d, e)
    numeros = list(map(int, lista))
    
    numeros.sort()
    
    resultado['text'] = numeros


#Funcion 2: 
#Multiplicar el número 1 con el 2 y se imprima las veces que está en el numero 5
from collections import Counter

def imprimir_texto():

    a = int(numero11.get())
    b = int(numero22.get())
    c = int(numero55.get())

    resultado['text']= a*b

#Funcion 3: 
def menornumero():
    a = int(numero11.get())
    b = int(numero22.get())
    c = int(numero33.get())
    d = int(numero44.get())
    e = int(numero55.get())

    numeros = [a, b, c, d, e] 
    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None
    
    if len(numeros) == 2 and numeros[0] == numeros[1]:
        return numeros [0]

    duplicados = set()
    unicos=[]

    for n in numeros:
        if n not in duplicados:
            duplicados.add(n)
            unicos.append(n)

    unicos.sort()
    return unicos[1]
    raise TypeError('El parámetro numeros deber ser una lista')
    salida1=(menornumero(numeros))

    menor=numeros[0]

    for i in range(0, len(numeros)):
        if numeros[i]<menor:
            menor=numeros[i]
    salida2 = 'el otro número menor es: ', menor


    resultado['text']=salida1*salida2

#Función 4
def mayornumero():
    a = int(numero11.get())
    b = int(numero22.get())
    c = int(numero33.get())
    d = int(numero44.get())
    e = int(numero55.get())

    lista=[a, b, c, d, e]
    alto=lista[0]

    for i in range(0, len(lista)):
        if lista[i]>alto:
            alto=lista[i]
    salida1 = 'el número mayor es: ', alto

    if isinstance(lista, list):
        if len(lista) < 2:
            return None

        if len(lista) == 2 and lista[0] == lista[1]:
            return None

        duplicados = set()
        unicos = []

        for n in lista:
            if n not in duplicados:
              duplicados.add(n)
              unicos.append(n)

    unicos.sort()
    return unicos[-2]

    salida2 = mayornumero, lista

    suma= salida1 + salida2
    multi=salida1 * salida2
    multiplicación= a*b*c*d*e - multi
    resultado['texto']= 'el resultado es: ', multiplicación - suma



#Funcion 5: numero primos

def primos():
    a=int(numero11.get())
    b = int(numero22.get())
    c = int(numero33.get())
    d = int(numero44.get())
    e = int(numero55.get())

    n=(a, b, c, d, e)
    x = list(map(int, n))
    contador=0
    resultado=True
    for i in range(1, n+1):
        if (n%i==0):
            contador+=1
        if (contador>2):
            resultado=False
            break
    return resultado
    if (primos(n)==True):
        resultado['texto']=("El número es primo", primos)
    else:
        resultado['texto']=("El resultado no es primo", primos)



#label en donde saldran las funciones
resultado = Label(window, text="Aquí se mostrarán las funciones", font=("Arial Bold", 10))
resultado.grid(row=8, column=1, columnspan=6) 

#botones de las funciones
btn = Button(window, text="Funcion1", command=ordenar, font=("Arial Bold", 11)).grid(column=1, row=7)
btn = Button(window, text="Funcion2", command=imprimir_texto, font=("Arial Bold", 11)).grid(column=2, row=7)
btn = Button(window, text="Funcion3", command=menornumero,font=("Arial Bold", 11)).grid(column=3, row=7)
btn = Button(window, text="Funcion4", command=mayornumero,font=("Arial Bold", 11)).grid(column=4, row=7)
btn = Button(window, text="Funcion5", command=primos, font=("Arial Bold", 11)).grid(column=5, row=7)


window.mainloop()