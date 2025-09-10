numerator=10
denominator=0


# De esta forma un puede hacer que el propagrama maneje un error sin que este deje de funcionar
# Por ejemplo una entrada inesperada del usuario
try:
    result=numerator/denominator
    print(result)
except:
    print("No es posible dividir entre cero")

    # SyntaxError: generado por el analizador sintactico cuando la sintaxis de Python esta mal
    # TypeErrorL: generado cuando se aplica una funcion u operacion a un objeto de tipo incorrecto
    # Name Error: generado cuando una variable nose encuentra en el entorno local o global
    # ZeroDivisionError: generado cuando se divide un valor o variable entre cero
    # IdentationError: ocurre cuando el codigo esta mal indentado
    #TabError: generado cuando las identaciones constan de tabulaciones o espacios incosistentes
