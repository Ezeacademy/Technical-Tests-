# Bank Installments Information

## cuestion: 

1 – You have the following object:

datos = {
	cuenta: "123456",
	nombre: "Juan",
	apellido: "Pérez",
	cuotas: [
		{ cuota: 13, importe: 123.4567 },
		{ cuota: 7, importe: 234.5678 },
		{ cuota: 2, importe: 456.7890 },
		{ cuota: 11, importe: 567.8901 },
		{ cuota: 3, importe: 678.9012 },
		{ cuota: 9, importe: 789.0123 },
		{ cuota: 12, importe: 890.1234 },
		{ cuota: 14, importe: 901.2345 },
		{ cuota: 8, importe: 12.3456 }
	]
}

The variable datos contains information about a bank customer's loan account.

datos.cuotas represents the outstanding installments for a loan taken by the customer, where each installment includes the installment number and its amount.

Let's assume:

The installment numbers range from 0 to N.
The installments are NOT sorted by installment number.
One or more installments may be missing, creating gaps in the array.
Your task is to develop a function that takes datos as a parameter and prints the user's account information along with the pending installments on the console.

Display the installment information in groups of consecutive installments, where each group shows:

Range of installment numbers, indicating the smallest and largest installment numbers separated by a hyphen.
Total amount for the range.
Sort the groups of consecutive installments in ascending order based on the installment number range.

Finally, show the overall total of the outstanding installment amounts.

For the given data at the beginning of the exercise, the output should be exactly as follows:

## Expected output:

Número de cuenta:  123456
Apellido y nombre: PÉREZ, Juan

Cuotas Pendientes: 2 - 3
Importe adeudado:  $1135.69

Cuotas Pendientes: 7 - 9
Importe adeudado:  $1035.93
 
Cuotas Pendientes: 11 - 14
Importe adeudado:  $2482.70
 
Total:             $4654.32

## Usage

1. Ensure you have Python installed on your machine.

2. Run the script with the provided example data:

```bash
python main.py
