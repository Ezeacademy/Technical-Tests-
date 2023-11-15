def mostrar_informacion(datos):
    # all information acount
    print("Número de cuenta:", datos["cuenta"])
    print("Apellido y nombre:", datos["apellido"].upper() + ",", datos["nombre"])

    # Sort installments by installment number
    cuotas_ordenadas = sorted(datos["cuotas"], key=lambda x: x["cuota"])

    print(cuotas_ordenadas)

    # Initialize variables for odds range and grand total
    rango_inicial = cuotas_ordenadas[0]["cuota"]
    rango_final = cuotas_ordenadas[-1]["cuota"]
    total_general = 0

    # Function to display the information of a range of quotas
    def mostrar_rango():
        nonlocal rango_inicial, rango_final
        importe_total = sum(cuota["importe"] for cuota in cuotas_ordenadas if rango_inicial <= cuota["cuota"] <= rango_final)
        print(importe_total)
        print(f"\nCuotas Pendientes: {rango_inicial} - {rango_final}")
        print(f"Importe adeudado: ${importe_total:.2f}\n")
        return importe_total

    # Function to determine if one installment is consecutive to another
    def es_consecutiva(cuota_anterior, cuota_actual):
        return cuota_actual - cuota_anterior == 1

    # browse quotas and show information
    for i in range(1, len(cuotas_ordenadas)):
        cuota_actual = cuotas_ordenadas[i]["cuota"]
        cuota_anterior = cuotas_ordenadas[i - 1]["cuota"]

        if es_consecutiva(cuota_anterior, cuota_actual):
            rango_final = cuota_actual
        else:
            total_general += mostrar_rango()
            rango_inicial = cuota_actual
            rango_final = cuota_actual

    # show total general
    total_general += mostrar_rango()

    # Show grand total
    print("Total: ${:.2f}".format(total_general))


# Example data
datos_ejemplo = {
    "cuenta": "123456",
    "nombre": "Juan",
    "apellido": "Pérez",
    "cuotas": [
        {"cuota": 13, "importe": 123.4567},
        {"cuota": 7, "importe": 234.5678},
        {"cuota": 2, "importe": 456.7890},
        {"cuota": 11, "importe": 567.8901},
        {"cuota": 3, "importe": 678.9012},
        {"cuota": 9, "importe": 789.0123},
        {"cuota": 12, "importe": 890.1234},
        {"cuota": 14, "importe": 901.2345},
        {"cuota": 8, "importe": 12.3456},
    ],
}
