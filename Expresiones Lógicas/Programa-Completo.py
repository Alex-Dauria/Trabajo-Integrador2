# Lista para almacenar los DNIs ingresados por el usuario
dnis = []
# Bucle para solicitar 5 DNIs
for i in range(5):
    while True:
        # Solicita un DNI y valida que tenga 8 dígitos numéricos
        dni = input(f"Ingrese el DNI {i+1} (8 dígitos): ")
        if len(dni) == 8 and dni.isdigit():
            dnis.append(dni)
            break
        else:
            # Si el DNI es válido, se agrega a la lista y se sale del bucle
            print("El DNI debe tener 8 dígitos numéricos.")

# Crear conjuntos de dígitos únicos y asignarlos a variables con nombres específicos
# Cada conjunto contiene los dígitos únicos del DNI correspondiente
conjunto_A = set(dnis[0])
conjunto_B = set(dnis[1])
conjunto_C = set(dnis[2])
conjunto_D = set(dnis[3])
conjunto_E = set(dnis[4])

# Mostrar los conjuntos de dígitos únicos
print(f"\nDígitos únicos del DNI 1 (Conjunto A): {sorted(conjunto_A)}")
print(f"Dígitos únicos del DNI 2 (Conjunto B): {sorted(conjunto_B)}")
print(f"Dígitos únicos del DNI 3 (Conjunto C): {sorted(conjunto_C)}")
print(f"Dígitos únicos del DNI 4 (Conjunto D): {sorted(conjunto_D)}")
print(f"Dígitos únicos del DNI 5 (Conjunto E): {sorted(conjunto_E)}")

# Calcular la unión de todos los conjuntos
union_todos = conjunto_A.union(conjunto_B, conjunto_C, conjunto_D, conjunto_E)
print(f"\nUnión de todos los conjuntos: {sorted(union_todos)}")

# Calcular intersecciones solicitadas
interseccion_A_B = conjunto_A.intersection(conjunto_B)
interseccion_C_D = conjunto_C.intersection(conjunto_D)
interseccion_D_E = conjunto_D.intersection(conjunto_E)
interseccion_todos = conjunto_A.intersection(conjunto_B, conjunto_C, conjunto_D, conjunto_E)

# Mostrar intersecciones
print(f"\nIntersección de Conjunto A y Conjunto B: {sorted(interseccion_A_B)}")
print(f"Intersección de Conjunto C y Conjunto D: {sorted(interseccion_C_D)}")
print(f"Intersección de Conjunto D y Conjunto E: {sorted(interseccion_D_E)}")
print(f"Intersección de todos los conjuntos: {sorted(interseccion_todos)}")

# Calcular diferencias solicitadas
diferencia_A_B = conjunto_A.difference(conjunto_B)
diferencia_C_D = conjunto_C.difference(conjunto_D)
diferencia_D_E = conjunto_D.difference(conjunto_E)

# Mostrar diferencias
print(f"\nDiferencia de Conjunto A menos Conjunto B: {sorted(diferencia_A_B)}")
print(f"Diferencia de Conjunto C menos Conjunto D: {sorted(diferencia_C_D)}")
print(f"Diferencia de Conjunto D menos Conjunto E: {sorted(diferencia_D_E)}")

# Calcular diferencias simétricas solicitadas
diferencia_simetrica_A_B = conjunto_A.symmetric_difference(conjunto_B)
diferencia_simetrica_C_D = conjunto_C.symmetric_difference(conjunto_D)
diferencia_simetrica_D_E = conjunto_D.symmetric_difference(conjunto_E)

# Mostrar diferencias simétricas
print(f"\nDiferencia simétrica de Conjunto A y Conjunto B: {sorted(diferencia_simetrica_A_B)}")
print(f"Diferencia simétrica de Conjunto C y Conjunto D: {sorted(diferencia_simetrica_C_D)}")
print(f"Diferencia simétrica de Conjunto D y Conjunto E: {sorted(diferencia_simetrica_D_E)}")

# Calcular la diferencia simétrica de todos los conjuntos
todos_conjuntos = [conjunto_A, conjunto_B, conjunto_C, conjunto_D, conjunto_E]
diferencia_simetrica_todos = set()
for elemento in union_todos:
    # Contar cuántas veces aparece el elemento en todos los conjuntos
    conteo = sum(1 for conjunto in todos_conjuntos if elemento in conjunto)
    # Incluir el elemento si aparece un número impar de veces
    if conteo % 2 == 1:
        diferencia_simetrica_todos.add(elemento)

# Mostrar la diferencia simétrica de todos los conjuntos
print(f"\nDiferencia simétrica de todos los conjuntos: {sorted(diferencia_simetrica_todos)}")

# Conteo de frecuencia de cada dígito en cada DNI
print("\nConteo de frecuencia de cada dígito en cada DNI:")
for i, dni in enumerate(dnis, 1):
    print(f"\nDNI {i}: {dni}")
    # Inicializar un diccionario para contar la frecuencia de cada dígito (0-9)
    frecuencia = {str(d): 0 for d in range(10)}
    # Contar la frecuencia de cada dígito en el DNI
    for digito in dni:
        frecuencia[digito] += 1
    # Mostrar solo los dígitos que aparecen al menos una vez
    print("Frecuencia de dígitos:")
    for digito, conteo in frecuencia.items():
        if conteo > 0:
            print(f"Dígito {digito}: {conteo} {'vez' if conteo == 1 else 'veces'}")

# Calcular la suma de los dígitos de cada DNI y la suma total
sumas_por_dni = []
total_digitos = 0

for dni in dnis:
    # Convertir cada dígito a entero y sumar
    suma_digitos = sum(int(digito) for digito in dni)  # Suma los dígitos de cada DNI
    sumas_por_dni.append((dni, suma_digitos))
    total_digitos += suma_digitos

# Mostrar resultados
print("\nDNIs ingresados y suma de sus dígitos:")
for dni, suma in sumas_por_dni:
    print(f"DNI: {dni}, Suma de dígitos: {suma}")
print(f"Suma total de todos los dígitos: {total_digitos}")

# Expresión lógica 1: Dígitos en A o B, pero no en C
# Usa unión para combinar A y B, y diferencia para excluir C
expresion_1 = (conjunto_A.union(conjunto_B)).difference(conjunto_C)
print(f"\nExpresión lógica 1: Dígitos en A o B, pero no en C: {sorted(expresion_1)}")

# Expresión lógica 2: Dígitos en D, pero no en la intersección de C y E
# Excluye los dígitos comunes de C y E del conjunto D
expresion_2 = conjunto_D.difference(conjunto_C.intersection(conjunto_E))
print(f"Expresión lógica 2: Dígitos en D, pero no en C ∩ E: {sorted(expresion_2)}")