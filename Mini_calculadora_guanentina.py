import math

def mini_calculadora():
    print("Mini Calculadora Guanentina")
    print("1 - Sumar (x + y)")
    print("2 - Restar (x - y)")
    print("3 - Multiplicar (x * y)")
    print("4 - Dividir (x / y)")
    print("5 - Potencia (x ^ y)")
    print("6 - Logaritmo (log base y de x)")
    
    try:
        x = float(input("Ingrese el valor de x: "))
        y = float(input("Ingrese el valor de y: "))
        opc = int(input("Seleccione una opción (1-6): "))

        if opc == 1:
            r = x + y
        elif opc == 2:
            r = x - y
        elif opc == 3:
            r = x * y
        elif opc == 4:
            if y != 0:
                r = x / y
            else:
                r = "No válido (división por cero)"
        elif opc == 5:
            r = x ** y
        elif opc == 6:
            if x > 0 and y > 0 and y != 1:
                r = math.log(x, y)
            else:
                r = "No válido (valores incorrectos para logaritmo)"
        else:
            r = "Opción no válida"
        
        print(f"Resultado: {r}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    mini_calculadora()
