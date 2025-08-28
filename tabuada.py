""" Imprime a tabuada do 1 ao 10.

Tabuada do 1 
1
2
3
...
_________________________________
Tabuada do 2
2
4
...
_________________________________

 """
__version__ = "1.0.0"
__author__ = "Camila Mota"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Interable (percorríveis)

# Para cada número em numeros
for numero in numeros:
    print("tabuada do numero:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-" * 30)