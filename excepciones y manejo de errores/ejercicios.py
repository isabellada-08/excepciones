
def ej_1():
    print("\n--- EJERCICIO 1: Conversión de edad ---")
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            print("Su edad es:", edad)
            break
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")

def ej_2():
    print("\n--- EJERCICIO 2: División segura ---")
    while True:
        try:
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo numero: "))
            resultado = numero1 / numero2
            print("Resultado:", resultado)
            break
        except ValueError:
            print("Error: debe ingresar numeros validos.\n")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.\n")

def ej_3():
    print("\n--- EJERCICIO 3: Acceso a una lista ---")
    nombres = ["Ana", "Carlos", "Maria", "Pedro"]
    while True:
        try:
            posicion = int(input("Ingrese la posicion del nombre (0-3): "))
            print("Nombre:", nombres[posicion])
            break
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")
        except IndexError:
            print("Error: esa posicion no existe.\n")

def ej_4():
    print("\n--- EJERCICIO 4: Consulta de cliente ---")
    clientes = {
        "001": ["Ana", "8888-1111"],
        "002": ["Carlos", "8888-2222"],
        "003": ["Maria", "8888-3333"]
    }
    while True:
        clave = input("Ingrese la clave del cliente (001, 002, 003): ")
        try:
            cliente = clientes[clave]
            print("Nombre:", cliente[0])
            print("Telefono:", cliente[1])
            break
        except KeyError:
            print("Error: el cliente no existe.\n")

def ej_5():
    print("\n--- EJERCICIO 5: Cierre garantizado ---")
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            resultado = 10 / numero
            print("Resultado:", resultado)
            break
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.\n")
        finally:
            print("La operacion ha terminado.")

def ej_6():
    print("\n--- EJERCICIO 6: Precio de un producto ---")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            print("Precio:", precio)
            break
        except ValueError:
            print("Error: el precio debe ser un numero.\n")

def ej_7():
    print("\n--- EJERCICIO 7: Cantidad de productos ---")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            print("Cantidad:", cantidad)
            break
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")

def ej_8():
    print("\n--- EJERCICIO 8: Calificación ---")
    while True:
        try:
            calificacion = float(input("Ingrese la calificacion (0 a 100): "))
            if calificacion >= 0 and calificacion <= 100:
                print("La calificacion esta entre 0 y 100.")
            else:
                print("La calificacion esta fuera del rango.")
            break
        except ValueError:
            print("Error: debe ingresar una calificacion numerica.\n")

def ej_9():
    print("\n--- EJERCICIO 9: Edad para registro ---")
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad >= 0 and edad <= 120:
                print("Edad valida.")
                break
            else:
                print("Error: la edad debe estar entre 0 y 120.\n")
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")

def ej_10():
    print("\n--- EJERCICIO 10: Tres entradas consecutivas ---")
    nombre = input("Ingrese su nombre: ")

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Error: la edad debe ser un numero entero.\n")

    while True:
        try:
            salario = float(input("Ingrese su salario: "))
            break
        except ValueError:
            print("Error: el salario debe ser un numero.\n")

    print("\nDatos ingresados correctamente.")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Salario:", salario)

def ej_11():
    print("\n--- EJERCICIO 11: Promedio de ventas ---")
    while True:
        try:
            venta1 = float(input("Ingrese la primera venta: "))
            venta2 = float(input("Ingrese la segunda venta: "))
            venta3 = float(input("Ingrese la tercera venta: "))

            total = venta1 + venta2 + venta3
            promedio = total / 3
            print("Promedio de ventas:", promedio)
            break
        except ValueError:
            print("Error: debe ingresar valores numericos.\n")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.\n")

def ej_12():
    print("\n--- EJERCICIO 12: Descuento proporcional ---")
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            base = float(input("Ingrese la base: "))
            porcentaje = (monto / base) * 100
            print("Porcentaje:", porcentaje, "%")
            break
        except ValueError:
            print("Error: debe ingresar numeros.\n")
        except ZeroDivisionError:
            print("Error: la base no puede ser cero.\n")

def ej_13():
    print("\n--- EJERCICIO 13: Conversión de moneda ---")
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            tasa = float(input("Ingrese la tasa de cambio: "))
            resultado = monto * tasa
            print("Monto convertido:", resultado)
            break
        except ValueError:
            print("Error: el monto y la tasa deben ser numeros.\n")

def ej_14():
    print("\n--- EJERCICIO 14: Tipos incompatibles ---")
    try:
        texto = "10"
        numero = 5
        resultado = texto + numero
        print(resultado)
    except TypeError:
        print("Error original: no se puede sumar un texto con un numero.")
        texto = int(texto)
        resultado = texto + numero
        print("Resultado corregido:", resultado)

def ej_15():
    print("\n--- EJERCICIO 15: Cálculo de comisión ---")
    while True:
        try:
            ventas = float(input("Ingrese el total de ventas: "))
            porcentaje = float(input("Ingrese el porcentaje de comision: "))
            comision = ventas * porcentaje / 100
            print("Comision:", comision)
            break
        except ValueError:
            print("Error: debe ingresar datos numericos.\n")

def ej_16():
    print("\n--- EJERCICIO 16: Índice de inventario ---")
    productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
    while True:
        try:
            posicion = int(input("Ingrese la posicion del producto (0-3): "))
            print("Producto:", productos[posicion])
            break
        except ValueError:
            print("Error: debe ingresar un numero entero.\n")
        except IndexError:
            print("Error: esa posicion no existe.\n")

def ej_17():
    print("\n--- EJERCICIO 17: Diccionario de empleados ---")
    empleados = {
        "001": "Ana",
        "002": "Carlos",
        "003": "Maria"
    }
    while True:
        clave = input("Ingrese la clave del empleado (001, 002, 003): ")
        try:
            print("Empleado:", empleados[clave])
            break
        except KeyError:
            print("Error: el empleado no existe.\n")

def ej_18():
    print("\n--- EJERCICIO 18: Menú de opciones ---")
    while True:
        print("\n1. Saludar")
        print("2. Mostrar mensaje")
        print("3. Salir")
        try:
            opcion2 = int(input("Seleccione una opcion: "))
            if opcion2 == 1:
                print("Hola, bienvenido.")
            elif opcion2 == 2:
                print("Esta es una opcion del menu.")
            elif opcion2 == 3:
                print("Ha seleccionado salir.")
            else:
                print("Error: opcion fuera del rango.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un numero valido.")

def ej_19():
    print("\n--- EJERCICIO 19: Archivo de reportes ---")
    try:
        archivo = open("reportes.txt", "r")
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("Error: el archivo reportes.txt no existe.")
    finally:
        print("La operacion del archivo ha terminado.")

def ej_20():
    print("\n--- EJERCICIO 20: Importación controlada ---")
    try:
        import modulo_que_no_existe
    except ModuleNotFoundError:
        print("Error: el modulo no existe.")
        print("Revise el nombre del modulo o instalelo correctamente.")