from Funciones import verificar_union_o_interseccion, es_grupo_sin_ceros

# Estos conjuntos se pasarán como argumentos a la función.
A = {0, 1, 2, 3, 4, 9}
B = {0, 1, 3, 5, 6, 8, 9}
C = {1, 2, 3, 6}
D = {0, 2, 4, 7, 9}
E = {0, 1, 3, 4, 9}


while True:
# Solicitar al usuario que ingrese un número a buscar.
    numero_ingresado = input("Ingrese un número entero positivo: ")
    if not numero_ingresado.isdigit() or int(numero_ingresado) < 1:
        print("Ingrese un número válido.")
    else:
        break

# Invocar la función y almacenar el resultado booleano.
# La función devuelve True o False directamente.
resultado_final = verificar_union_o_interseccion(A, B, C, D, E, int(numero_ingresado))

print(f"¿El número {numero_ingresado} se encuentra en la unión de todos los conjuntos, o la intersección de todos los conjuntos está vacía?")

# Imprimir la respuesta con el resultado booleano.
if resultado_final:
    print("Respuesta: VERDADERO. Al menos una de las opciones se cumple.")
else:
    print("Respuesta: FALSO. Ninguna de las dos opciones se cumple.")


# Evaluar si es un grupo sin ceros usando la segunda función.
resultado_sin_ceros = es_grupo_sin_ceros(A, B, C, D, E)

print("¿Es un grupo sin ceros?")
# Imprimir la respuesta de la segunda condición.
if resultado_sin_ceros:
    print("Respuesta: VERDADERO. Es un grupo sin ceros.")
else:
    print("Respuesta: FALSO. NO es un grupo sin ceros.")