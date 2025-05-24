""" 
Verifica si el número ingresado está entre los elementos de la unión,
o si la intersección general entre los elementos del conjunto está vacía.

Python cuenta con métodos para trabajar directamente con los conjuntos, como union() e intersection().
"""

# Función para verificar la unión entre los conjuntos A, B, C, D y E.
def verificar_union_o_interseccion(conjunto_a, conjunto_b, conjunto_c, conjunto_d, conjunto_e, numero_ingresado):
    # Calcular la unión de todos los conjuntos.
    union_todos = conjunto_a.union(conjunto_b, conjunto_c, conjunto_d, conjunto_e)
    
    # Primera condición: ¿El número está en la unión?
    condicion_numero_en_union = (numero_ingresado in union_todos)
    
    # Evaluar si la intersección de todos los conjuntos es un conjunto vacío.
    interseccion_todos = conjunto_a.intersection(conjunto_b, conjunto_c, conjunto_d, conjunto_e)
    
    # Segunda condición: ¿La intersección está vacía?
    condicion_interseccion_vacia = (len(interseccion_todos) == 0)
    
    # Combinar ambas condiciones con el operador lógico OR y retornar el resultado.
    return condicion_numero_en_union or condicion_interseccion_vacia


# Función para verificar si ningún conjunto contiene el número 0.
def es_grupo_sin_ceros(conjunto_a, conjunto_b, conjunto_c, conjunto_d, conjunto_e):
    return (
        0 not in conjunto_a and
        0 not in conjunto_b and
        0 not in conjunto_c and
        0 not in conjunto_d and
        0 not in conjunto_e
    )
