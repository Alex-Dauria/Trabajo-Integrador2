def ingreso_anio_nacimiento():
    # Función para ingresar los años de nacimiento de los integrantes
    anios = []
    miembros = int(input("Ingrese la cantidad de integrantes que hay en el grupo: "))
    
    for i in range(miembros):
        while True:
            try:
                # Ingreso de año de nacimiento por el usuario
                anio = int(input(f"Ingresá el año de nacimiento del integrante {i + 1}: "))

                #Verificar si el año se repite
                if anio in anios:
                    print("Ese año ya fue ingresado. Ingresá uno distinto")
                    continue

                # Verificar que el año ingresado este en un rango lógico
                if anio < 1900 or anio > 2025:
                    print("Ingrese un año entre 1900 y 2025.")
                    continue # Vuelve al principio del while

                anios.append(anio)
                break # Si todo está bien, sale del while
            except ValueError:
                print("Ingrese un año válido")
    return anios


def cont_pares_impares(anios):
    # Cuenta cuántos años son pares y cuántos impares en la lista recibida
    pares = 0
    impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def verificar_grupo_z(anios):
    # Verifica si todos los integrantes nacieron después del año 2000
    for anio in anios:
        if anio <= 2000:
            return False # No es Grupo Z
    return True # Todos nacieron despues del 2000 -> Grupo Z

def es_bisiesto(anio):
    #Es bisiesto si es divisible por 4 y NO es divisible por 100 o es divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def verificar_bisiesto(anios):
    # Recorre los años para verificar si alguno es bisiesto
    # Imprime un mensaje si encuentra al menos uno
    for anio in anios:
        if es_bisiesto(anio):
            print("\nTenemos un año especial")
            break

def calcular_edades(anios, anio_actual = 2025):
    # Verificamos las edades a partir de los años ingresados y el año actual
    edades = [anio_actual - anio for anio in anios]
    return edades

def producto_cartesiano(anios, edades):
    # Calcula el producto cartesiano entre la lista de años y la lista de edades
    # Devuelve una lista de tuplas (año, edad) con todas las combinaciones posibles
    producto_car = [(anio, edad) for anio in anios for edad in edades]
    return producto_car

# Programa Principal
def main():
    print("\nOperaciones con años de nacimiento")

    #Ingreso de los años de nacimiento
    anios_nacimiento = ingreso_anio_nacimiento()
    print(f"\nAños ingresados: {anios_nacimiento}")

    # Contador de años pares impares
    pares, impares = cont_pares_impares(anios_nacimiento)
    print(f"\nCantidad de miembros que nacieron en años pares: {pares}")
    print(f"Cantidad de miembros que nacieron en años impares: {impares}")

    # Verificación Grupo Z

    if verificar_grupo_z(anios_nacimiento):
        print("\nGrupo Z")

    # Imprimir años bisiestos
    verificar_bisiesto(anios_nacimiento)

    # Calculo de edades
    edades = calcular_edades(anios_nacimiento)
    print(f"\nEdades actuales en 2025: {edades}")

    # Calculo de producto cartesiano entre años y edades
    product_car = producto_cartesiano(anios_nacimiento, edades)
    print("\nProducto cartesiano de edades y años de nacimiento")
    for anio, edad in product_car:
        print(f"Año: {anio}, Edad: {edad}")
        
if __name__ == "__main__":
    main()