numerator=10
denominator=0


# De esta forma un puede hacer que el propagrama maneje un error sin que este deje de funcionar
# Por ejemplo una entrada inesperada del usuario
try:
    result=numerator/denominator
    print(result)
except:
    print("No es posible dividir entre cero")
