def mostrar_informacion(datos):
    # Extract account information
    cuenta = datos["cuenta"]
    apellido = datos["apellido"].upper()
    nombre = datos["nombre"]

    # Sort installments by installment number
    cuotas_ordenadas = sorted(datos["cuotas"], key=lambda x: x["cuota"])

    total_general = 0

    # Function to display the information of a range of installments
    def mostrar_rango(rango_inicial, rango_final):
        # Calculate the total amount for the specified installment range
        importe_total = sum(cuota["importe"] for cuota in cuotas_ordenadas if rango_inicial <= cuota["cuota"] <= rango_final)
        # Print information for the installment range
        print(importe_total)
        print(f"\nCuotas Pendientes: {rango_inicial} - {rango_final}")
        print(f"Importe adeudado: ${importe_total:.2f}\n")
        return importe_total

    # Function to determine if one installment is consecutive to another
    def es_consecutiva(cuota_anterior, cuota_actual):
        return cuota_actual - cuota_anterior == 1

    # Initialize variables for the installment range
    rango_inicial = cuotas_ordenadas[0]["cuota"]
    rango_final = rango_inicial

    # Iterate through installments to display information
    for i in range(1, len(cuotas_ordenadas)):
        cuota_actual = cuotas_ordenadas[i]["cuota"]
        cuota_anterior = cuotas_ordenadas[i - 1]["cuota"]

        # Check if the current installment is consecutive to the previous one
        if es_consecutiva(cuota_anterior, cuota_actual):
            rango_final = cuota_actual
        else:
            # Display information for the current installment range and update total
            total_general += mostrar_rango(rango_inicial, rango_final)
            rango_inicial = cuota_actual
            rango_final = cuota_actual

    # Display information for the last installment range
    total_general += mostrar_rango(rango_inicial, rango_final)

    # Display account information and grand total
    print(f"Número de cuenta: {cuenta}")
    print(f"Apellido y nombre: {apellido}, {nombre}")
    print(cuotas_ordenadas)
    print(f"Total: ${total_general:.2f}")


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
