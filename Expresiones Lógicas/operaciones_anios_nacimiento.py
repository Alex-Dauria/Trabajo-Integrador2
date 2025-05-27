def es_bisiesto(anio):
# bisiesto. Un año es bisiesto si es divisible por 4, Excepto si es divisible por 100, no es bisiesto 
# A menos que también sea divisible por 400, entonces sí es bisiesto
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    else:
        return anio % 400 == 0

def ingresar_anios_nacimiento():
    # Función para ingresar los años de nacimiento de los integrantes.
    anios = []
    cantidad = int(input("¿Cuántos integrantes tiene el grupo? "))
    
    for i in range(cantidad):
        while True:
            try:
                anio = int(input(f"Ingrese el año de nacimiento del integrante {i+1}: "))
                if anio < 1900 or anio > 2025:  # Rango razonable
                    print("Por favor ingrese un año entre 1900 y 2025.")
                    continue
                
                # Verificar si el año ya fue ingresado
                if anio in anios:
                    print("Este año ya fue ingresado. Por favor ingrese un año diferente.")
                    continue
                    
                anios.append(anio)
                break
            except ValueError:
                print("Por favor ingrese un año válido (número entero).")
    
    return anios

def contar_pares_impares(anios):
    # años son pares e impares
    pares = 0
    impares = 0
    
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

def verificar_grupo_z(anios):
    # si todos nacieron después del 2000
    return all(anio > 2000 for anio in anios)

def verificar_anio_bisiesto(anios):
    # si algún año es bisiesto
    return any(es_bisiesto(anio) for anio in anios)

def calcular_edades(anios, anio_actual=2025):
    # edades actuales a partir de los años de nacimiento
    return [anio_actual - anio for anio in anios]

def producto_cartesiano(anios, edades):
    #  Calcula el producto cartesiano entre años de nacimiento y edades
    # Devuelve una lista de tuplas (año, edad)
    return [(anio, edad) for anio in anios for edad in edades]

def main():
    print("\n--- Operaciones con años de nacimiento ---\n")
    
    # Ingreso de años de nacimiento
    anios_nacimiento = ingresar_anios_nacimiento()
    print(f"\nAños de nacimiento ingresados: {sorted(anios_nacimiento)}")
    
    # Contar años pares e impares
    pares, impares = contar_pares_impares(anios_nacimiento)
    print(f"\nNacieron en años pares: {pares} integrantes")
    print(f"Nacieron en años impares: {impares} integrantes")
    
    # Verificar si todos nacieron después del 2000
    if verificar_grupo_z(anios_nacimiento):
        print("\nGrupo Z (todos nacieron después del 2000)")
    
    # Verificar si hay años bisiestos
    if verificar_anio_bisiesto(anios_nacimiento):
        print("\nTenemos un año especial (al menos uno nació en año bisiesto)")
    
    # Mostrar qué años son bisiestos
    bisiestos = [anio for anio in anios_nacimiento if es_bisiesto(anio)]
    if bisiestos:
        print(f"Años bisiestos en el grupo: {bisiestos}")
    
    # Calcular edades actuales
    edades = calcular_edades(anios_nacimiento)
    print(f"\nEdades actuales (2025): {edades}")
    
    # Calcular producto cartesiano entre años y edades
    cartesiano = producto_cartesiano(anios_nacimiento, edades)
    print("\nProducto cartesiano entre años de nacimiento y edades:")
    for par in cartesiano:
        print(f"Año: {par[0]}, Edad: {par[1]}")

if __name__ == "__main__":
    main()