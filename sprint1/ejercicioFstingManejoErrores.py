a=100
b=0
c=10
d='a'

#Primera division
numerador=a
denominador=b
try:
    result=numerador/denominador
    print(f"El resultado de dividir {numerador} entre {denominador} es {result}")
except ZeroDivisionError:
    print(f"No puedes dividir {numerador} entre {denominador}")

print()
#Segunda division
numerador=a
denominador=c
try:
    result=numerador/denominador
    print(f"El resultado de dividir {numerador} entre {denominador} es {result}")
except ZeroDivisionError:
    print(f"No puedes dividir {numerador} entre {denominador}")

print()
#Tercera division

numerador=a
denominador=d
try:
    result=numerador/denominador
    print(f"El resultado de dividir {numerador} entre {denominador} es {result}")
except TypeError:
    print(f"No puedes dividir {numerador} entre {denominador} ya que este segundo es un string")