# Importamos la hoja de ejercicios
import ejercicios

while True:
    print("\n======================================")
    print("---------------- Menu ----------------")
    print("======================================")
    print("1. Conversion de edad")
    print("2. Division segura")
    print("3. Acceso a una lista")
    print("4. Consulta de cliente")
    print("5. Cierre garantizado")
    print("6. Precio de un producto")
    print("7. Cantidad de productos")
    print("8. Calificacion")
    print("9. Edad para registro")
    print("10. Tres entradas consecutivas")
    print("11. Promedio de ventas")
    print("12. Descuento proporcional")
    print("13. Conversion de moneda")
    print("14. Tipos incompatibles")
    print("15. Calculo de comision")
    print("16. Indice de inventario")
    print("17. Diccionario de empleados")
    print("18. Menu de opciones")
    print("19. Archivo de reportes")
    print("20. Importacion controlada")
    print("0. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        ejercicios.ej_1()
    elif opcion == "2":
        ejercicios.ej_2()
    elif opcion == "3":
        ejercicios.ej_3()
    elif opcion == "4":
        ejercicios.ej_4()
    elif opcion == "5":
        ejercicios.ej_5()
    elif opcion == "6":
        ejercicios.ej_6()
    elif opcion == "7":
        ejercicios.ej_7()
    elif opcion == "8":
        ejercicios.ej_8()
    elif opcion == "9":
        ejercicios.ej_9()
    elif opcion == "10":
        ejercicios.ej_10()
    elif opcion == "11":
        ejercicios.ej_11()
    elif opcion == "12":
        ejercicios.ej_12()
    elif opcion == "13":
        ejercicios.ej_13()
    elif opcion == "14":
        ejercicios.ej_14()
    elif opcion == "15":
        ejercicios.ej_15()
    elif opcion == "16":
        ejercicios.ej_16()
    elif opcion == "17":
        ejercicios.ej_17()
    elif opcion == "18":
        ejercicios.ej_18()
    elif opcion == "19":
        ejercicios.ej_19()
    elif opcion == "20":
        ejercicios.ej_20()
    elif opcion == "0":
        print("\nPrograma finalizado.")
        break
    else:
        print("\nError: opcion no valida.")

    input("\nPresione ENTER para volver al menu...")