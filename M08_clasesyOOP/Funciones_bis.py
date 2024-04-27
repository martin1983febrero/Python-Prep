# ENCAPSULAMIENTO --- genero un ciclo for para que tome los elementos de la lista
# Uso las mismas funciones (pero ENCAPSULADAS CON __ guiones bajos) pero ahora las INVOCO

#----------------------------LO NUEVO------------------------------------
class Funciones_bis:
    def __init__(self,listado):  
        self.lista = listado                  
    
    def verifica_primo(self):
        for i in self.lista:   # iterará sobre la LISTA INICIAL elemento a elemento
            if self.__verifica_primo(i): 
                print(f'El {i} es PRIMO')
            else:
                print(f'El {i} NO es PRIMO')

    def verifica_conversion_grados(self,origen,destino):
        for i in self.lista:   # lo mismo
            print(f'{i} grados {origen} es equivalente a {self.__verifica_conversion_grados(i,origen,destino)} grados {destino}')        
#--------self.__verifica_conversion_grados(i,origen,destino)-------------
#--------------------Esto es lo dificil de entender----------------------

    def verifica_factorial(self):
        for i in self.lista:   # lo mismo
            print(f'El factorial de {i} es {self.__verifica_factorial(i)}')
            # Me daba error porque faltaba {self.__verifica_factorial(i)}


#------LO MISMO DE ANTES PERO ENCAPSULADO (excepto VALOR MODAL)-----------
    def __verifica_primo(self,valor): # va sin =
        primo = True
        for i in range(2,valor): # Me daba error porque en ves de for puse otro if :)
            if valor % i == 0: # Quiere decir que si existe divisor intermedio, además del divisor 1 y el número, entonces no será primo
                primo = False            
        return(primo)
        
    def verifica_valor_modal(self):   # CORRECCIÓN: le dejé solo (self) y en COUNTER puse -> (self.lista)
        # Debo incorporar COUNTER de la LIBRERIA
        #---------------------------------------
        from collections import Counter
        #---------------------------------------
        dic_counter = Counter(self.lista) # SE VERÁ: Counter({5: 5, 1: 2, 2: 2, 6: 2, 4: 2, 3: 1, 8: 1, 54: 1, 656: 1})
        mas_repetido = max(dic_counter, key = dic_counter.get)
        cuantas = dic_counter[mas_repetido]
        return  print(f'El número más repetido en la lista es el {mas_repetido} y se repitió {cuantas} veces')
    
    def __verifica_conversion_grados(self,valor, origen,destino): 
    
        if origen == 'Celsius':
            if destino == 'Farenheit':
                celcius_farenheit = (valor * (9/5)) + 32
                rta = celcius_farenheit
            elif destino == 'Kelvin':
                celsius_kelvin = valor + 273.15
                rta = celsius_kelvin
            else:
                celsius_celsius = valor
                rta = celsius_celsius
        
        if origen == 'Farenheit':
            if destino == 'Celsius':
                farenheit_celsius = (valor -32) * (5/9)
                rta = farenheit_celsius
            elif destino == 'Kelvin':
                farenheit_kelvin = ((valor -32) * (5/9)) + 273.15
                rta = farenheit_kelvin
            else:
                farenheit_farenheit = valor
                rta = farenheit_farenheit
        
        if origen == 'Kelvin':
            if destino == 'Celsius':
                kelvin_celsius = valor - 273.15
                rta = kelvin_celsius
            elif destino == 'Farenheit':
                kelvin_farenheit = ((valor - 273.15) * (9/5)) + 32
                rta = kelvin_farenheit
            else:
                kelvin_kelvin = valor
                rta = kelvin_kelvin
        return rta
    
    def __verifica_factorial(self,n):
        
        if (type(n) == int):
            
            if (n > 0):
                factorial = n
                while (n>2):
                    n = n - 1
                    factorial = factorial * n
                return factorial
            elif n == 0:
                return print(' 0 por definición')
            else:
                return print('ERROR. La variable no es mayor a cero')
        else:
            return print('ERROR. La variable no es un entero')